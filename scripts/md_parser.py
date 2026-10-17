"""
md_parser.py
Clean, robust markdown to HTML parser tailored for the Kenaley Longevity Protocol wiki.
"""

import re

def simple_markdown_to_html(md_text):
    # Normalize line endings
    text = md_text.replace('\r\n', '\n').strip()
    
    # 1. Protect currency like $10, $15, $350 - $500 so they aren't parsed as math delimiters
    text = re.sub(r'\$(\d+(?:\.\d+)?)', r'&#36;\1', text)
    
    # 2. Extract code blocks (triple backticks) to placeholders
    code_blocks = []
    def save_code_block(m):
        code = m.group(2).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        idx = len(code_blocks)
        code_blocks.append(f'<pre class="code-block"><code>{code}</code></pre>')
        return f"\n\n<!--CODE_BLOCK_{idx}-->\n\n"
    text = re.sub(r'```([a-zA-Z0-9_-]*)\n(.*?)```', save_code_block, text, flags=re.DOTALL)

    # 3. Extract tables to placeholders
    tables = []
    lines = text.split('\n')
    new_lines = []
    in_table = False
    curr_table = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            in_table = True
            curr_table.append(line)
        else:
            if in_table:
                idx = len(tables)
                tables.append(render_markdown_table(curr_table))
                new_lines.append(f"\n<!--TABLE_BLOCK_{idx}-->\n")
                curr_table = []
                in_table = False
            new_lines.append(line)
    if in_table:
        idx = len(tables)
        tables.append(render_markdown_table(curr_table))
        new_lines.append(f"\n<!--TABLE_BLOCK_{idx}-->\n")
        
    text = '\n'.join(new_lines)

    # 4. Inline code (single backticks)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    
    # 5. LaTeX math
    text = re.sub(r'\\\((.*?)\\\)', r'<code class="math-inline">\1</code>', text)
    text = re.sub(r'\\\[(.*?)\\\]', r'<div class="math-block"><code>\1</code></div>', text, flags=re.DOTALL)
    text = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-block"><code>\1</code></div>', text, flags=re.DOTALL)
    text = re.sub(r'\$([^\$]+?)\$', r'<code class="math-inline">\1</code>', text)

    # 6. Formatting (Bold / Italic)
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    # 7. Blockquotes and Alerts
    text = re.sub(r'^> \[!NOTE\]\s*(.*?)$', r'<div class="alert alert-note"><p>\1</p></div>', text, flags=re.MULTILINE)
    text = re.sub(r'^> \[!TIP\]\s*(.*?)$', r'<div class="alert alert-tip"><p>\1</p></div>', text, flags=re.MULTILINE)
    text = re.sub(r'^> \[!WARNING\]\s*(.*?)$', r'<div class="alert alert-warning"><p>\1</p></div>', text, flags=re.MULTILINE)
    text = re.sub(r'^> (.*?)$', r'<blockquote><p>\1</p></blockquote>', text, flags=re.MULTILINE)

    # 8. Headers with clean blank line spacing
    text = re.sub(r'\n*^### (.*?)$\n*', r'\n\n<h3>\1</h3>\n\n', text, flags=re.MULTILINE)
    text = re.sub(r'\n*^## (.*?)$\n*', r'\n\n<h2>\1</h2>\n\n', text, flags=re.MULTILINE)
    text = re.sub(r'\n*^# (.*?)$\n*', r'\n\n<h1>\1</h1>\n\n', text, flags=re.MULTILINE)
    
    # 9. Horizontal Rules
    text = re.sub(r'\n*^---\s*$\n*', r'\n\n<hr class="divider"/>\n\n', text, flags=re.MULTILINE)

    # 10. Split into distinct blocks by 2+ newlines
    raw_blocks = [b.strip() for b in text.split('\n\n') if b.strip()]
    processed_blocks = []

    for block in raw_blocks:
        # Check if block is a placeholder or already HTML tag
        if block.startswith('<!--CODE_BLOCK_'):
            idx = int(re.search(r'CODE_BLOCK_(\d+)', block).group(1))
            processed_blocks.append(code_blocks[idx])
        elif block.startswith('<!--TABLE_BLOCK_'):
            idx = int(re.search(r'TABLE_BLOCK_(\d+)', block).group(1))
            processed_blocks.append(tables[idx])
        elif any(block.startswith(h) for h in ['<h1>', '<h2>', '<h3>', '<h4>', '<hr', '<div class="alert', '<blockquote', '<div class="math-block']):
            processed_blocks.append(block)
        elif block.startswith('- ') or block.startswith('* ') or re.match(r'^\d+\.\s+', block):
            # Process list
            list_lines = block.split('\n')
            is_ol = bool(re.match(r'^\d+\.\s+', list_lines[0].strip()))
            tag = 'ol' if is_ol else 'ul'
            out = [f'<{tag}>']
            for l in list_lines:
                clean_l = l.strip()
                if not clean_l:
                    continue
                clean_l = re.sub(r'^[-*]\s+', '', clean_l)
                clean_l = re.sub(r'^\d+\.\s+', '', clean_l)
                out.append(f'  <li>{clean_l}</li>')
            out.append(f'</{tag}>')
            processed_blocks.append('\n'.join(out))
        else:
            # Wrap as standard paragraph, convert single newlines to <br/>
            clean_p = block.replace('\n', '<br/>')
            processed_blocks.append(f'<p>{clean_p}</p>')

    return '\n\n'.join(processed_blocks)

def render_markdown_table(table_lines):
    if len(table_lines) < 2:
        return "\n".join(table_lines)
    
    header_cols = [c.strip() for c in table_lines[0].strip().strip('|').split('|')]
    rows = []
    for row_line in table_lines[2:]:
        cols = [c.strip() for c in row_line.strip().strip('|').split('|')]
        rows.append(cols)
        
    out = ['<div class="table-container"><table class="data-table">', '  <thead><tr>']
    for h in header_cols:
        out.append(f'    <th>{h}</th>')
    out.append('  </tr></thead><tbody>')
    for r in rows:
        out.append('  <tr>')
        for col in r:
            out.append(f'    <td>{col}</td>')
        out.append('  </tr>')
    out.append('  </tbody></table></div>')
    return "\n".join(out)
