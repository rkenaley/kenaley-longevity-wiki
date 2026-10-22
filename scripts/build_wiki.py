"""
build_wiki.py
Generates the complete, self-contained Kenaley Longevity Protocol v5.0 Wiki Web Repository.
- Creates assets/css/style.css, assets/css/modules.css
- Creates assets/js/data.js, assets/js/main.js
- Converts all 40 intervention markdown modules into rich, linked HTML subpages in modules/
- Creates the central index.html with interactive tabs, searchable spreadsheet, 24h timeline,
  infradian matrix, physical pillbox matrix, precision recipes, and athletic BMT hub.
"""

import os
import csv
import json
import re
from md_parser import simple_markdown_to_html

WIKI_DIR = r"d:\Ryan Files 2026\06_Health_and_Wellness\kenaley-longevity-wiki"
INTERVENTIONS_DIR = r"d:\Ryan Files 2026\06_Health_and_Wellness\Whitepaper_v4_Rewrite\interventions"
CSV_PATH = os.path.join(WIKI_DIR, "Kenaley_Protocol_Interventions_Index.csv")

os.makedirs(os.path.join(WIKI_DIR, "assets", "css"), exist_ok=True)
os.makedirs(os.path.join(WIKI_DIR, "assets", "js"), exist_ok=True)
os.makedirs(os.path.join(WIKI_DIR, "assets", "images"), exist_ok=True)
os.makedirs(os.path.join(WIKI_DIR, "modules"), exist_ok=True)

# Image mapping for each module
MODULE_IMAGES = {
    1: [
        {"file": "Type 2 Diabetes Metabolic Diagram.jpg", "caption": "Cecal Starch Shunting & Peripheral Glucose Regulation"},
        {"file": "insulin crp.jpg", "caption": "Insulin Sensitivity & Systemic Glycemic Control"},
        {"file": "Exercise-training-coupled-with-vinegar-intake-may-improve-glucose-uptake-and-increase.ppm.png", "caption": "Acidic Acetic Acid / Vinegar Substrate Synergies"}
    ],
    8: [
        {"file": "atherosclerosis summary.PNG", "caption": "Atherogenesis Cascade: ApoB Particle Transcytosis & Subendothelial Retention"},
        {"file": "causes of death.png", "caption": "All-Cause Mortality vs Lifetime Cumulative ApoB Exposure"},
        {"file": "blueprint supplements.png", "caption": "Comparative Longevity Biomarker & Lipid Deceleration Targets"}
    ],
    9: [
        {"file": "atherosclerosis summary.PNG", "caption": "Matrix Gla Protein (MGP) Activation & Vascular Elastin Decalcification"}
    ],
    11: [
        {"file": "atherosclerosis summary.PNG", "caption": "Low-Attenuation Vulnerable Soft Plaque Volumetric Regression (Budoff 2016)"}
    ],
    15: [
        {"file": "Stem CEll Factors.jpg", "caption": "Therapeutic Plasma Dilution: Evacuation of Circulating Pro-Aging Factors"}
    ],
    17: [
        {"file": "Steroidogenesis.svg.png", "caption": "Endogenous Steroidogenesis Cascade: Preserving LH/FSH & Testicular Output"}
    ],
    18: [
        {"file": "Steroidogenesis.svg.png", "caption": "Suicidal Aromatase Inhibition: Irreversible Inactivation of CYP19A1"}
    ],
    20: [
        {"file": "Epitalon divide these doses by 10.PNG", "caption": "Epitalon Pineal Bioregulator: Microdose vs Supraphysiological Human Sizing"}
    ],
    22: [
        {"file": "nootropics_image1a.png", "caption": "Nigrostriatal Dopaminergic Protection & MAO-B Catalytic Cleavage"}
    ],
    23: [
        {"file": "Yamanake molecules.PNG", "caption": "TET-Mediated 5mC DNA Demethylation & Yamanaka Epigenetic Reprogramming Factors"}
    ],
    26: [
        {"file": "nootropics_image1a.png", "caption": "AMPA Receptor Allosteric Modulation & Neuronal Membrane Fluidity"}
    ],
    27: [
        {"file": "nootropics_image1a.png", "caption": "Targeted Dopaminergic & Neurotrophic Apothecary Kinetics"},
        {"file": "TCDS Inthinkerator circuit.PNG", "caption": "Direct Neuromodulation Circuitry & Synaptic Plasticity Priming"}
    ],
    28: [
        {"file": "TrumpkinGoodSauna01.3j.png", "caption": "Finnish Thermal Sauna Architecture & Convective Heat Cavity (Trumpkin Model)"},
        {"file": "sauna_rules.jpeg", "caption": "Thermal Physiology: Convective Stratification, Löyly Dynamics & HSP70 Induction"}
    ],
    29: [
        {"file": "Stem CEll Factors.jpg", "caption": "The Hyperoxic-Hypoxic Paradox: HIF-1alpha Stabilization & Endogenous Stem Cell Spikes"}
    ],
    31: [
        {"file": "TCDS Inthinkerator circuit.PNG", "caption": "Transcutaneous Auricular Vagus Nerve Stimulation (taVNS) Neuromodulation"}
    ],
    37: [
        {"file": "Genotype-Diet.png", "caption": "Nutrigenomic Substrate Routing & Precision Macronutrient Partitioning"},
        {"file": "insulin crp.jpg", "caption": "Postprandial Insulin Blunting via RS3 Resistant Starch Retrogradation"},
        {"file": "intraworkout.PNG", "caption": "Nutrient Partitioning & Functional Hydration Architecture"}
    ],
    38: [
        {"file": "the-catapult-mechanism-elastic-recoil-of-fascial-tissues-4-600x867.png", "caption": "The Catapult Mechanism: Fascial Elastic Recoil & Collagen Micro-Tendon Architecture"},
        {"file": "French Contrast Method.png", "caption": "French Contrast / Triphasic Loading Progression: Heavy Potentiation into Explosive Elasticity"},
        {"file": "Deitz FC.png", "caption": "Cal Dietz Triphasic Elastic Potentiation Framework"},
        {"file": "triphasic template.PNG", "caption": "Weekly High-Intensity Elastic Neuromuscular Split"},
        {"file": "triphasic template 2.PNG", "caption": "Triphasic Periodization Waves & Rate of Force Development (RFD)"},
        {"file": "Block_Training.png", "caption": "Neuromuscular Block Periodization: Explosive Elastic & Sprint Wave Loading"},
        {"file": "Single LEg reactive strength index.PNG", "caption": "Reactive Strength Index (RSI) & Unilateral Elastic Stiffness"},
        {"file": "foot pressure drills.PNG", "caption": "Biomechanical Foot & Ankle Elastic Spring Loading Drills"},
        {"file": "Expected-Physiological-Adaptations-in-Sweet-Spot_9e492cf9-c77a-4765-be0e-a6b945f3a25a_1024x1024.png", "caption": "Off-Day Zone 2 Aerobic Base & Capillary Density Adaptations"},
        {"file": "Exercise Benefits.jpg", "caption": "Systemic Exercise Adaptations: Endothelial Shear, Neurogenesis & Myokine Secretion"}
    ],
    39: [
        {"file": "Stem CEll Factors.jpg", "caption": "FMD Refeeding Cycle: Hematopoietic & Mesenchymal Stem Cell Surge"},
        {"file": "Antiaging Summary.jpg", "caption": "Autophagic Clearance & Multi-System Rejuvenation Dynamics"}
    ],
    40: [
        {"file": "Epitalon divide these doses by 10.PNG", "caption": "Infradian Peptide Pulses: Pineal Epitalon 10-Day Semiannual Reset"},
        {"file": "Stem CEll Factors.jpg", "caption": "Infradian Regenerative Niche: TPE & FMD Stem Cell Mobilization"},
        {"file": "Yamanake molecules.PNG", "caption": "Long-Term Epigenetic Drift Interception via Periodic Infradian Cadence"}
    ],
    41: [
        {"file": "Stem CEll Factors.jpg", "caption": "PAI-1 Inhibition: Hematopoietic Stem Cell Mobilization & Epigenetic Clock Reversal"},
        {"file": "Antiaging Summary.jpg", "caption": "SASP Suppression & Extracellular Matrix Microvascular Restoration"}
    ],
    42: [
        {"file": "stem_cell_macrocycle_panel1.png", "caption": "Panel 1: 12-Week Macro-Cycle — Sequential Niche Purification, Priming & Mobilization"}
    ]
}

def get_html_filename(mod_num, name=""):
    slug_map = {
        1: "01_acarbose.html", 2: "02_taurine.html", 3: "03_turnbuckle.html", 4: "04_ss31_ergothioneine.html",
        5: "05_pqq.html", 6: "06_urolithin_a.html", 7: "07_spermidine.html", 8: "08_apob_eradication.html",
        9: "09_vitamin_k2_mk7.html", 10: "10_microdose_tadalafil.html", 11: "11_aged_garlic_sac.html",
        12: "12_krill_oil_mfsd2a.html", 13: "13_olive_leaf_oleuropein.html", 14: "14_mayo_fisetin.html",
        15: "15_pascoe_plasmapheresis.html", 16: "16_albumin_reconstitution.html", 17: "17_enclomiphene.html",
        18: "18_exemestane.html", 19: "19_ipamorelin_cjc1295.html", 20: "20_epitalon.html",
        21: "21_shbg_displacement.html", 22: "22_selegiline_microdose.html", 23: "23_calcium_akg.html",
        24: "24_cats_claw_ac11.html", 25: "25_lithium_orotate.html", 26: "26_piracetam_cdp_choline.html",
        27: "27_experimental_apothecary.html", 28: "28_finnish_thermal_sauna.html", 29: "29_protocolized_hbot.html",
        30: "30_photobiomodulation_pbm.html", 31: "31_sleep_architecture_tavns.html", 32: "32_topical_dermatology.html",
        33: "33_environmental_defense.html", 34: "34_oral_microbiome_nitrate.html", 35: "35_cardiolipin_remodeling.html",
        36: "36_ecm_glycation_defense.html", 37: "37_precision_nutrition_recipes.html", 38: "38_athletic_bmt_sprinting.html",
        39: "39_longo_fmd.html", 40: "40_infradian_pulsed_cadence.html", 41: "41_tm5614_oral_pai1_inhibitor.html",
        42: "42_stem_cell_niche_expansion.html"
    }
    return slug_map.get(mod_num, f"{mod_num:02d}.html")

def parse_csv_data():
    items = []
    with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items

def build_data_js(items):
    js_content = f"// Kenaley Protocol Interventions Dataset\nwindow.PROTOCOL_DATA = {json.dumps(items, indent=2)};\n"
    with open(os.path.join(WIKI_DIR, "assets", "js", "data.js"), "w", encoding="utf-8") as f:
        f.write(js_content)
    print("assets/js/data.js generated successfully.")

def build_subpages(csv_items):
    print("Building all 42 module subpages...")
    
    csv_by_mod = {}
    for item in csv_items:
        m = re.match(r"INT-(\d+)", item.get("ID", ""))
        if m:
            csv_by_mod[int(m.group(1))] = item

    for mod_num in range(1, 43):
        matches = [f for f in os.listdir(INTERVENTIONS_DIR) if re.match(rf"^{mod_num:02d}_.*\.md$", f)]
        if not matches:
            print(f"Warning: No markdown found for module {mod_num}")
            continue
        
        md_filename = matches[0]
        md_path = os.path.join(INTERVENTIONS_DIR, md_filename)
        with open(md_path, "r", encoding="utf-8") as f:
            md_raw = f.read()

        html_filename = get_html_filename(mod_num)
        subpage_path = os.path.join(WIKI_DIR, "modules", html_filename)

        csv_row = csv_by_mod.get(mod_num, {})
        interv_name = csv_row.get("Intervention", md_filename.replace(".md", ""))
        pillar = csv_row.get("Biological Pillar", "Systems Biology")
        tier = csv_row.get("Conviction Tier", "CORE BET")
        grade = csv_row.get("Evidence Grade", "E1/E2")
        cost = csv_row.get("Est. Monthly Cost ($/mo)", "$15 - $25 / month")
        p_val = csv_row.get("P(Healthspan %)", "80%")
        hallmark = csv_row.get("Target Hallmark", "Cellular Senescence & Mitochondrial Dysfunction")
        stance = csv_row.get("Stance", "Contrarian")

        body_html = simple_markdown_to_html(md_raw)

        images_html = ""
        if mod_num in MODULE_IMAGES:
            images_html += '<div class="module-visuals"><h2>Spidered Biological & Protocol Visualizations</h2>'
            for img in MODULE_IMAGES[mod_num]:
                images_html += f"""
                <div class="img-card">
                  <img src="../assets/images/{img['file']}" alt="{img['caption']}" loading="lazy">
                  <div class="img-caption">{img['caption']}</div>
                </div>
                """
            images_html += '</div>'

        prev_link_html = ""
        if mod_num > 1:
            prev_file = get_html_filename(mod_num - 1)
            prev_row = csv_by_mod.get(mod_num - 1, {})
            prev_title = f"INT-{mod_num-1:02d}: {prev_row.get('Intervention', '')}"
            prev_link_html = f"""
            <a href="{prev_file}" class="nav-module-btn">
              <span class="nav-module-dir">&larr; Previous Module</span>
              <span class="nav-module-title">{prev_title}</span>
            </a>
            """
        else:
            prev_link_html = '<div></div>'

        next_link_html = ""
        if mod_num < 42:
            next_file = get_html_filename(mod_num + 1)
            next_row = csv_by_mod.get(mod_num + 1, {})
            next_title = f"INT-{mod_num+1:02d}: {next_row.get('Intervention', '')}"
            next_link_html = f"""
            <a href="{next_file}" class="nav-module-btn" style="text-align: right; margin-left: auto;">
              <span class="nav-module-dir">Next Module &rarr;</span>
              <span class="nav-module-title">{next_title}</span>
            </a>
            """
        else:
            next_link_html = '<div></div>'

        full_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>INT-{mod_num:02d}: {interv_name} | Kenaley Longevity Protocol v5.0</title>
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/modules.css">
</head>
<body>
  <nav class="navbar">
    <div class="nav-brand">
      <a href="../index.html" style="color: inherit; text-decoration: none; display: flex; align-items: center; gap: 0.5rem;">
        <span>KENALEY PROTOCOL</span>
        <span class="nav-brand-badge">v5.0 WIKI</span>
      </a>
    </div>
    <div class="nav-links">
      <a href="../index.html" class="nav-link">&larr; Back to Wiki Hub</a>
      <a href="../index.html#spreadsheet" class="nav-link">Master Index</a>
      <a href="../index.html#timeline" class="nav-link">24h Schedule</a>
      <a href="../index.html#infradian" class="nav-link">Infradian</a>
      <a href="../index.html#pillbox" class="nav-link">Pillbox</a>
      <a href="../index.html#recipes" class="nav-link">Kitchen</a>
      <a href="../index.html#athletic" class="nav-link">BMT Athletic</a>
    </div>
    <div class="nav-actions">
      <a href="../KENALEY_LONGEVITY_V5_MASTER_LLM.md" class="btn btn-secondary btn-sm" download>LLM Master .md</a>
      <button id="theme-toggle" class="btn btn-secondary btn-sm" aria-label="Toggle theme">☀️</button>
    </div>
  </nav>

  <main class="module-layout">
    <div class="breadcrumb-nav">
      <a href="../index.html">Wiki Home</a>
      <span>&rsaquo;</span>
      <span>{pillar}</span>
      <span>&rsaquo;</span>
      <span style="color: var(--accent-blue);">INT-{mod_num:02d}</span>
    </div>

    <header class="module-header">
      <div class="module-id-badge">INT-{mod_num:02d}</div>
      <h1 class="module-title">{interv_name}</h1>
      <div class="module-badges">
        <span class="badge badge-core">{tier}</span>
        <span class="badge badge-pillar">{pillar}</span>
        <span class="badge badge-high">Evidence: {grade}</span>
        <span class="badge badge-exploratory">Est. Cost: {cost}</span>
        <span class="badge badge-core">P(Healthspan): {p_val}</span>
      </div>
      <div class="metadata-grid">
        <div class="meta-item">
          <span class="meta-label">Primary Target Hallmark</span>
          <span class="meta-value">{hallmark}</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Protocol Stance</span>
          <span class="meta-value">{stance}</span>
        </div>
        <div class="meta-item">
          <span class="meta-label">Source Document</span>
          <span class="meta-value"><code>{md_filename}</code></span>
        </div>
      </div>
    </header>

    <article class="module-content">
      {body_html}
      {images_html}
    </article>

    <footer class="module-nav-footer">
      {prev_link_html}
      {next_link_html}
    </footer>
  </main>

  <footer class="footer">
    <div class="footer-links">
      <a href="../index.html">Wiki Hub</a>
      <a href="../KENALEY_LONGEVITY_V5_MASTER_LLM.md">Lossless LLM Master</a>
      <a href="../Kenaley_Longevity_Whitepaper_v5.pdf">Compiled PDF Whitepaper</a>
      <a href="../Kenaley_Pillbox_Matrix_Card.pdf">Printable Pillbox PDF</a>
    </div>
    <p>Kenaley Longevity Protocol v5.0 &copy; 2026 Ryan Kenaley. Rejuvenation Olympics Benchmark.</p>
  </footer>

  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
        with open(subpage_path, "w", encoding="utf-8") as f:
            f.write(full_html)
            
    print(f"Generated subpages in {os.path.join(WIKI_DIR, 'modules')}")

def main():
    print("Re-running Kenaley Longevity Protocol Wiki Build with refined markdown parser...")
    csv_items = parse_csv_data()
    build_data_js(csv_items)
    build_subpages(csv_items)
    print("Wiki subpages regenerated successfully!")

if __name__ == "__main__":
    main()
