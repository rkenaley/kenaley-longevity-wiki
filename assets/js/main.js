// Kenaley Protocol v5.0 Interactive Wiki Engine
document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  initThemeToggle();
  initSearch();
  initImageModal();
  renderSpreadsheetTable(window.PROTOCOL_DATA || []);
});

// Tab Switching
function initTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');
  
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      
      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(p => p.classList.remove('active'));
      
      btn.classList.add('active');
      const pane = document.getElementById(target);
      if (pane) pane.classList.add('active');
      
      // Update URL hash
      window.location.hash = target;
    });
  });

  // Check URL hash on load
  if (window.location.hash) {
    const hash = window.location.hash.replace('#', '');
    const activeBtn = document.querySelector(`.tab-btn[data-tab="${hash}"]`);
    if (activeBtn) activeBtn.click();
  }
}

// Theme Toggle
function initThemeToggle() {
  const themeBtn = document.getElementById('theme-toggle');
  if (!themeBtn) return;
  
  const currentTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
  updateThemeIcon(themeBtn, currentTheme);

  themeBtn.addEventListener('click', () => {
    const active = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = active === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeIcon(themeBtn, next);
  });
}

function updateThemeIcon(btn, theme) {
  btn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
  btn.title = `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`;
}

// Search and Filter
function initSearch() {
  const searchInput = document.getElementById('main-search');
  const pillarSelect = document.getElementById('filter-pillar');
  const tierSelect = document.getElementById('filter-tier');

  function triggerFilter() {
    const q = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const pillar = pillarSelect ? pillarSelect.value : 'all';
    const tier = tierSelect ? tierSelect.value : 'all';
    
    if (!window.PROTOCOL_DATA) return;
    
    const filtered = window.PROTOCOL_DATA.filter(item => {
      const matchesQ = !q || 
        (item.ID && item.ID.toLowerCase().includes(q)) ||
        (item.Intervention && item.Intervention.toLowerCase().includes(q)) ||
        (item['Target Hallmark'] && item['Target Hallmark'].toLowerCase().includes(q)) ||
        (item['Biophysical Mechanism'] && item['Biophysical Mechanism'].toLowerCase().includes(q)) ||
        (item['Surveillance Biomarkers'] && item['Surveillance Biomarkers'].toLowerCase().includes(q));
      
      const matchesPillar = (pillar === 'all') || (item['Biological Pillar'] && item['Biological Pillar'].includes(pillar));
      const matchesTier = (tier === 'all') || (item['Conviction Tier'] && item['Conviction Tier'].includes(tier));

      return matchesQ && matchesPillar && matchesTier;
    });

    renderSpreadsheetTable(filtered);
  }

  if (searchInput) searchInput.addEventListener('input', triggerFilter);
  if (pillarSelect) pillarSelect.addEventListener('change', triggerFilter);
  if (tierSelect) tierSelect.addEventListener('change', triggerFilter);
  
  // Keyboard shortcut '/' focuses search
  window.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      if (searchInput) searchInput.focus();
    }
  });
}

// Render Spreadsheet Table
function renderSpreadsheetTable(data) {
  const tbody = document.getElementById('spreadsheet-body');
  const countEl = document.getElementById('record-count');
  if (!tbody) return;
  
  if (countEl) countEl.innerText = `${data.length} Interventions`;

  if (data.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 2rem; color: var(--text-muted);">No interventions matched your search filters.</td></tr>`;
    return;
  }

  let html = '';
  data.forEach(item => {
    const id = item.ID || '';
    const name = item.Intervention || '';
    const pillar = item['Biological Pillar'] || '';
    const tier = item['Conviction Tier'] || '';
    const grade = item['Evidence Grade'] || '';
    const cost = item['Est. Monthly Cost ($/mo)'] || '';
    const pVal = item['P(Healthspan %)'] || '';
    const link = item['Artifact Link'] || '';
    
    // Map to subpage HTML
    let subpageUrl = '#';
    const numMatch = id.match(/INT-(\d+)/);
    if (numMatch) {
      const modNum = parseInt(numMatch[1], 10);
      subpageUrl = `modules/${getModuleHtmlName(modNum)}`;
    }

    const tierBadgeClass = getTierBadgeClass(tier);

    html += `
      <tr>
        <td style="font-family: var(--font-mono); font-weight: 700; color: var(--accent-blue);">
          <a href="${subpageUrl}">${id}</a>
        </td>
        <td>
          <a href="${subpageUrl}" style="font-weight: 600; color: var(--text-primary);">
            ${name}
          </a>
        </td>
        <td><span class="badge badge-pillar">${formatPillarShort(pillar)}</span></td>
        <td><span class="badge ${tierBadgeClass}">${tier}</span></td>
        <td style="font-family: var(--font-mono); font-size: 0.8rem;">${grade}</td>
        <td style="font-weight: 700; color: var(--accent-emerald);">${pVal}</td>
        <td style="color: var(--text-secondary);">${cost}</td>
      </tr>
    `;
  });

  tbody.innerHTML = html;
}

function getTierBadgeClass(tier) {
  if (tier.includes('CORE')) return 'badge-core';
  if (tier.includes('HIGH')) return 'badge-high';
  if (tier.includes('EXPLORATORY')) return 'badge-exploratory';
  if (tier.includes('EXPERIMENTAL')) return 'badge-experimental';
  if (tier.includes('RETIRED')) return 'badge-retired';
  return 'badge-core';
}

function formatPillarShort(pillar) {
  if (pillar.includes('Metabolic')) return 'Metabolic';
  if (pillar.includes('Mitochondrial')) return 'Mitochondrial';
  if (pillar.includes('Cardiovascular')) return 'Cardiovascular';
  if (pillar.includes('Senescence')) return 'Senolytics/TPE';
  if (pillar.includes('Endocrine')) return 'Endocrine';
  if (pillar.includes('Neuro')) return 'Neuro/Apothecary';
  if (pillar.includes('Systems')) return 'Systems/Hardware';
  return pillar;
}

function getModuleHtmlName(modNum) {
  const map = {
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
    39: "39_longo_fmd.html", 40: "40_infradian_pulsed_cadence.html"
  };
  return map[modNum] || `${modNum}.html`;
}

// Image Zoom Modal
function initImageModal() {
  const modal = document.createElement('div');
  modal.className = 'modal-overlay';
  modal.innerHTML = `
    <div class="modal-content">
      <button class="modal-close" aria-label="Close">&times;</button>
      <img src="" alt="Enlarged Diagram">
    </div>
  `;
  document.body.appendChild(modal);

  const modalImg = modal.querySelector('img');
  const closeBtn = modal.querySelector('.modal-close');

  document.addEventListener('click', (e) => {
    if (e.target.matches('.img-card img')) {
      modalImg.src = e.target.src;
      modal.classList.add('active');
    }
  });

  closeBtn.addEventListener('click', () => modal.classList.remove('active'));
  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });
}
