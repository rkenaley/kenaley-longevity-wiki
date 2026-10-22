"""
build_master_llm.py
Generates the comprehensive, lossless master markdown document (KENALEY_LONGEVITY_V5_MASTER_LLM.md)
for the Kenaley Longevity Protocol v5.0, designed for drag-and-drop into modern LLMs (Claude 3.5 Sonnet,
GPT-4o, Gemini 1.5/2.0 Pro) with zero context loss.
"""

import os
import glob
import re

ROOT_DIR = r"d:\Ryan Files 2026\06_Health_and_Wellness"
INTERVENTIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "interventions")
PILLBOX_MD_PATH = os.path.join(ROOT_DIR, "Kenaley_Pillbox_Matrix_Card.md")
OUT_PATH = os.path.join(ROOT_DIR, "kenaley-longevity-wiki", "KENALEY_LONGEVITY_V5_MASTER_LLM.md")

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def get_intervention_files():
    files = glob.glob(os.path.join(INTERVENTIONS_DIR, "*.md"))
    # filter out README.md
    files = [f for f in files if not os.path.basename(f).startswith("README")]
    # sort by module number
    def sort_key(f):
        m = re.match(r"(\d+)_", os.path.basename(f))
        return int(m.group(1)) if m else 999
    return sorted(files, key=sort_key)

def main():
    print("Generating Lossless LLM Master Markdown...")
    
    interv_files = get_intervention_files()
    print(f"Found {len(interv_files)} intervention markdown modules.")

    pillbox_content = load_file(PILLBOX_MD_PATH)

    doc = []
    
    # 1. Document Header & LLM Meta-Instructions
    doc.append("""# THE KENALEY LONGEVITY PROTOCOL v5.0: MASTER COMPREHENSIVE ARCHITECTURE
**The Complete Lossless Biophysical Whitepaper, Clinical Dispensary, Nutrition, Athletic & Infradian Ledger**  
*Author: Ryan Kenaley*  
*Standard: Rejuvenation Olympics Benchmark (DunedinPACE < 0.45, OMICmAge Deceleration, ApoB < 35 mg/dL)*  
*Document Version: 5.0 (Architectural Edition)*  
*Export Format: Fully Lossless Markdown for Direct LLM Context Injection*

---

> [!NOTE]
> ## INSTRUCTIONS FOR THE ARTIFICIAL INTELLIGENCE / LLM (CLAUDE, GPT-4O, GEMINI)
> You are analyzing the **Kenaley Longevity Protocol v5.0**, an advanced, biophysically grounded human rejuvenation protocol. This file contains the complete, unabridged, lossless architecture of the protocol:
> 1. **Core Philosophy & 7 Biological Pillars**
> 2. **Universal Table Stakes & Lifestyle Foundation**
> 3. **The 24-Hour Master Chrono-Architecture (Daily Circadian Schedule 06:30 - 22:30)**
> 4. **The Physical 4-Slot Pillbox Dispensing Matrix & Lab Fridge Storage**
> 5. **Precision Longevity Kitchen & Powder Smoothie Architecture (Module 37)**
> 6. **Athletic Performance Architecture: Zac Goodman BMT, Dynamic Tendon Recoil & CNS Sprinting (Module 38)**
> 7. **Valter Longo 5-Day Fasting Mimicking Diet (FMD) & Autophagic Purge (Module 39)**
> 8. **The Infradian Master Architecture: Monthly to Annual Pulsed Protocols (Module 40)**
> 9. **The Complete 42-Module Interventions Ledger (Dosing, Pharmacokinetics, Biophysical Mechanisms, Cofactors, Failure Modes, Surveillance Biomarkers, Kill Criteria, Epistemic Frontier Questions)**
> 10. **The Epistemic Graveyard (Retired Interventions & Rationale)**
> 11. **Comprehensive Drug-Drug Interaction & Kinetic Collision Safety Matrix**
> 12. **Surveillance Biomarker Reference Ranges & Laboratory Testing Schedule**
>
> **HOW YOU MUST RESPOND WHEN QUERIED ON THIS PROTOCOL:**
> - **Act as an elite Longevity Physician-Biophysicist** versed in molecular biology, pharmacology, endocrinology, and biomechanics.
> - **Cross-reference user questions against the exact 42 modules, pillbox slots, and kinetic collision rules.**
> - **Biomarker Analysis:** When the user provides their personal lab test results (ApoB, hsCRP, cystatin C, HbA1c, HOMA-IR, Total/Free Testosterone, Estradiol, LH, FSH, SHBG, IGF-1, etc.), compare them strictly against the quantified target reference ranges in this whitepaper. Identify out-of-range markers, highlight underlying biophysical drivers, and suggest specific titration adjustments or cofactors according to the protocol rules.
> - **Personalized Recommendations:** Always respect the separation between daily maintenance and infradian pulses (e.g., never take senolytics or mitochondrial fission inducers continuously; maintain the strict separation between AMPK/autophagy windows and post-workout mTOR/hypertrophy windows; observe acarbose starch requirements).
> - **Safety First:** If a proposed compound or dose risks drug-drug interactions (e.g., Tadalafil + Nitrates, Acarbose on zero-carb meals, Selegiline + high-dose Tyramine, high-dose unchelated minerals, or excessive aromatase inhibition), immediately flag the contraindication with clear biochemical explanations.

---

# SECTION I: PROTOCOL PHILOSOPHY & THE SEVEN BIOLOGICAL PILLARS

## 1.1 Operating Philosophy: Asymmetric Expected Value & Mechanistic Rigor
The Kenaley Longevity Protocol is constructed on the premise of **Asymmetric Expected Value (EV)**. Human clinical trials for maximum lifespan extension cannot be completed within actionable time horizons. Therefore, the protocol combines:
1. Multi-organism lifespan validation (NIA Interventions Testing Program - ITP).
2. Human randomized controlled surrogate trials (reversal of soft plaque, arterial pulse wave velocity, biological epigenetic clock deceleration).
3. First-principles biophysical plausibility (mitochondrial cristae curvature, electron transport chain tunneling, endothelial glycocalyx preservation, chaperone-mediated autophagy).

Every intervention is classified under an **Evidence Grade (E1 to E5)** and assigned a Bayesian Probability of Real Human Healthspan Extension:
- **E1 (Gold Standard):** Human double-blind RCTs with hard clinical endpoints or validated surrogate biomarkers.
- **E2 (Strong Human Surrogate):** Human RCTs demonstrating intermediate physiological reversal (e.g., flow-mediated dilation, CAC regression, epigenetic age reduction).
- **E3 (Human Pilot / Mechanistic):** Pharmacokinetic, observational, or small-scale proof-of-concept human trials.
- **E4 (Robust Mammalian Lifespan):** Gold-standard replicated rodent lifespan extension (e.g., NIA ITP).
- **E5 (Cellular / Non-Mammalian In Vitro):** Mechanistic models in yeast, C. elegans, or cell culture.

## 1.2 The Seven Biological Pillars
1. **Pillar I: Metabolic Substrate Flexibility & Nutrient Sensing** (Modules 01, 02, 37)  
   Suppression of postprandial glucose excursions, enhancement of cecal starch fermentation into butyrate, mitochondrial tRNA taurinylation, and dietary substrate modulation.
2. **Pillar II: Mitochondrial Dynamics, IMM Latching & Mitophagy** (Modules 03, 04, 05, 06, 07, 35)  
   Restoration of inner mitochondrial membrane (IMM) cristae architecture via cardiolipin protection (SS-31, DLPC), biogenesis (PQQ), mitophagy (Urolithin A), hypusination-driven autophagy (Spermidine), and cyclic fission/fusion clearing.
3. **Pillar III: Cardiovascular Hemodynamics, Endothelial Glycocalyx & Atherosclerosis Eradication** (Modules 08, 09, 10, 11, 12, 13, 34)  
   Aggressive lifetime ApoB reduction (<35 mg/dL), heparan sulfate endothelial glycocalyx shielding, continuous microdose cGMP/eNOS tone, vascular elastin decalcification (K2 MK-7), and enterosalivary nitrate engine activation.
4. **Pillar IV: Cellular Senescence, Senolytics & Hematological Cleansing** (Modules 14, 15, 16, 41, 42)  
   Intermittent hit-and-run senolytic clearance of senescent cells (Mayo pulsed Fisetin), oral PAI-1 serpin inhibition for stem cell niche rejuvenation (TM5614), therapeutic donor plasmapheresis / neutral blood exchange (TPE) to dilute pro-aging systemic circulating factors, immediate albumin/electrolyte remineralization, and the 12-week Stem Cell Niche Purification and Mobilization Macro-Cycle (Module 42).
5. **Pillar V: Endocrine Homeostasis, Anabolic Maintenance & Pulsatile Peptides** (Modules 17, 18, 19, 20, 21)  
   Preservation of youthful androgenic and growth hormone signaling without axis shutdown: pure trans-enclomiphene microdosing, suicidal aromatase titration (exemestane), nocturnal pulsatile GHRH/GHRP secretagogues (Ipamorelin/CJC-1295), SHBG displacement, and pineal bioregulation (Epitalon).
6. **Pillar VI: Neuro-Endocrine Optimization, Nootropics & Neuroprotection** (Modules 22, 23, 24, 25, 26, 27)  
   Sub-microdose MAO-B inhibition for nigrostriatal dopamine preservation (Paul Kiesow selegiline), TET-mediated DNA demethylation (Calcium-AKG), PARP-1 DNA repair (AC-11), GSK-3beta inhibition (lithium orotate), cholinergic membrane fluidity (piracetam/CDP-choline), and neurotrophic apothecary support.
7. **Pillar VII: Systems Biology, Hardware & Environmental Engineering** (Modules 28, 29, 30, 31, 32, 33, 36, 38, 39, 40)  
   Finnish thermal hyperthermia (HSP70), protocolized HBOT hyperoxic-hypoxic stem cell triggers, systemic 660/850nm photobiomodulation, glymphatic sleep architecture (taVNS & mouth taping), dermatological retinoid/GHK-Cu remodeling, multi-barrier air/water purification, extracellular matrix crosslink defense, BMT dynamic athletic performance, 5-day FMD fasting cycles, and the overarching infradian pulse cadence.

## 1.3 The Compact 8-Tier Functional Taxonomy (Operational Clustering)
To achieve maximal operational compactness and clear functional synergy, the 42 interventions are consolidated into eight high-yield operational engines:

1. **Tier 1: Postprandial Glycemic Shield & Anti-Glycation Engine** (Modules 01, 36, 37, 38)
   • Acarbose (25–50 mg) competitive brush-border α-glucosidase delay & cecal starch shunting
   • Cyanidin-3-Glucoside / C3G (300–330 mg active) SGLT1/GLUT2 inhibition & SIRT6 allostery
   • Postprandial Box Squats (15–25 reps) & Soleus Pushups contraction-mediated non-insulin GLUT4 clearance
   • Retrograded RS3 Resistant Starch double-helix crystallization
   • Extracellular Matrix Carbonyl Trapping (Benfotiamine 300 mg, Carnosine 1,000 mg, Pyridoxamine 50 mg)
2. **Tier 2: Mitochondrial Cristae Integrity & Organellar Remodeling Suite** (Modules 02, 03, 04, 05, 06, 35)
   • Tafazzin substrate loading (DLPC), SS-31 cardiolipin electrostatic shielding, Taurine mt-tRNA translation, PQQ biogenesis, and Urolithin A mitophagy.
3. **Tier 3: Hemodynamic, Endothelial & Calcification Defense Core** (Modules 08, 09, 10, 11, 13, 34)
   • ApoB eradication (<35 mg/dL), Vitamin K2 MK-7 matrix decalcification, microdose Tadalafil cGMP tone, Aged Garlic SAC plaque regression, and enterosalivary nitrate engine.
4. **Tier 4: Epigenetic Programming, Chromatin Stability & DNA Repair Axis** (Modules 20, 23, 24, 37, 41)
   • Calcium-AKG TET1–3 DNA demethylation, Cat's Claw AC-11 PARP/NER stimulation, SIRT6 H3K9/56 deacetylation, and Epitalon pineal telomerase induction.
5. **Tier 5: Neuro-Dopaminergic & Cognitive Plasticity Vector** (Modules 12, 22, 25, 26, 27, 31)
   • Sub-microdose Selegiline MAO-B protection, Low-Dose Lithium GSK-3β/BDNF, Piracetam AMPA fluidity, Krill LPC-DHA MFSD2A transport, and glymphatic AQP4 clearance.
6. **Tier 6: Endocrine Pulsing, Steroidogenesis & Anabolic Preservation Cluster** (Modules 17, 18, 19, 21, 38)
   • Pure trans-enclomiphene SERM, exemestane suicidal aromatase control, SHBG displacement, pulsatile GH secretagogues / travel OKG stack, and BMT dynamic tendon loading.
7. **Tier 7: Systemic Cellular Cleansing, Senolysis & Proteome Dilution Suite (Infradian)** (Modules 07, 14, 15, 16, 39, 40, 41, 42)
   • TM5614 oral PAI-1 serpin inhibition, Mayo pulsed Fisetin senolysis, Spermidine autophagy, Valter Longo 5-day FMD, Pascoe donor plasmapheresis (TPE), albumin reconstitution, and 12-week Stem Cell Niche Purification and Mobilization Macro-Cycle (Module 42).
8. **Tier 8: Biophysical Environmental & Thermal Hardware Foundation** (Modules 28, 29, 30, 32, 33)
   • Finnish thermal sauna (HSP70), protocolized HBOT hyperoxic-hypoxic stem cell mobilization, 660/850nm photobiomodulation, HEPA/carbon/RO environmental purity, and topical retinoids/GHK-Cu.


---

# SECTION II: THE ASSUMED BASELINE (UNIVERSAL TABLE STAKES)
Prior to initiating pharmacological or pulsed biohacks, the following non-negotiable foundations must be operational:
1. **Sleep Architecture:** Minimum 7.5 to 8.5 hours in a cold (65-68°F / 18-20°C), pitch-black room (<0.5 lux). Nasal breathing enforced via mouth tape. Zero caffeine within 10 hours of sleep.
2. **Hydration & Water Purity:** Multi-stage reverse osmosis (RO) purification with remineralization. Daily intake of 3.0 to 4.0 liters with adequate sodium, potassium, and magnesium.
3. **Photobiology & Circadian Entrainment:** 10 to 20 minutes of direct morning sunlight within 30 minutes of waking. Minimization of blue light (450-480nm) after sunset via blue-blocking eyewear or software filters.
4. **Nutritional Quality:** Whole food, nutrient-dense diet emphasizing polyphenols, diverse fiber (>40g/day), healthy lipid profiles (extra virgin olive oil, wild fatty fish), and avoidance of advanced glycation end-products (charred meat), industrial seed oils (high linoleic acid), and ultra-processed refined carbohydrates.
5. **Toxicological Defense:** Zero tobacco, zero vaping, minimal to zero ethanol, rigorous avoidance of plastics (BPA/BPS, phthalates), HEPA/activated carbon filtration in living spaces.

---
""")

    # 2. Section III: The Master 24-Hour Chrono-Architecture
    doc.append("""# SECTION III: THE MASTER 24-HOUR CHRONO-ARCHITECTURE (CIRCADIAN PROTOCOL)

The protocol organizes all pharmacological, nutritional, and physical interventions into strict circadian windows to eliminate kinetic collisions, prevent receptor cross-tolerance, and align with natural physiological oscillators:

### 06:30 - 07:00 | Circadian Awakening & Cortisol Awakening Surge
- **Photobiology:** Step outside for 10-15 minutes of direct solar photon exposure to reset the suprachiasmatic nucleus (SCN).
- **Hydration:** 20-24 oz (600-750 mL) purified RO water with a pinch of Celtic sea salt / potassium bicarbonate.
- **Dispensing:** **Pillbox Slot 1 (AM Fasted)** swallowed with water.
  - Urolithin A (1,000 mg)
  - Spermidine (15-20 mg)
  - Calcium-AKG (1,000 mg) + Liposomal Vitamin C (500 mg) + Apigenin (50 mg)
  - Microdose Tadalafil (2.5 - 5.0 mg)
  - Low-Dose Lithium Orotate (5 mg elemental)
  - Cat's Claw AC-11 (350 - 700 mg)
- **Sublingual / Mon-Wed-Fri Only:** Selegiline (0.25 mg sublingual). *Allow to absorb under tongue for 5 minutes; do not swallow whole.*
- **Oral Protocol (Module 34):** Tongue scraping followed by remineralizing nano-hydroxyapatite brushing. *Strictly avoid chlorhexidine or alcohol-based mouthwashes.*

### 07:00 - 11:30 | Fasted Deep Work & Cognitive Focus Window
- Maximum cognitive clarity period powered by high fasted dopamine and low insulin.
- Optional morning warm collagen broth drink (Module 37: 15g Hydrolyzed Bovine/Marine Collagen Peptides + broth base + 500mg Liposomal Vitamin C) if training late or needing joint nourishment without insulin spikes.
- Pure black coffee or ceremonial green tea (EGCG).

### 11:30 - 12:00 | Pre-Workout Joint & Fascial Priming
- If not consumed at waking: Drink the 15g Collagen Broth Drink with Liposomal Vitamin C 30-45 minutes prior to mechanical loading to maximize proline/hydroxyproline delivery to avascular tendon matrix.

### 12:00 - 13:15 | High-Intensity Athletic Training Window (Module 38: BMT)
- Dynamic fascial warmup & multi-planar ankle/foot prep.
- Rolling A/B/A periodization:
  - **Day A:** Heavy paused box squats, DB weighted jumps, elastic hurdle plyos, secondary hinge (RDL / Nordic curl).
  - **Day B:** Thrower's bench press, fresh-CNS 10-30m maximum-velocity sprints, explosive upper plyos.
  - **Off Days:** 45-60 min Zone 2 steady-state nasal cardio (120-135 bpm) + fascial foam rolling and mobility.

### 13:30 - 14:15 | Post-Workout Nutrition & Main Refuel (Meal 1)
- The primary carbohydrate and protein meal of the day.
- **Core Carbohydrate Source:** Pressure-Cooker Retrograded RS3 Resistant Starch (Module 37: cooled white rice / sweet potatoes / oats) providing high amylose retrogradation and minimal glycemic impact.
- **Lean Protein Source:** Wild salmon, pasture-raised chicken breast, or lean bison (40-50g protein).
- **Dispensing:** **Pillbox Slot 2 (Midday / Meal 1)**:
  - **Acarbose (25 - 50 mg):** *CRITICAL: Take with the absolute first forkful of complex carbohydrates.*
  - Bempedoic Acid (180 mg) + Ezetimibe (10 mg)
  - Citrus Bergamot (500 mg)
  - Vitamin K2 MK-7 (200 mcg) + Vitamin D3 (3,000 IU) + Retinol (2,500 IU)
  - Kyolic Aged Garlic Extract (600 mg) + Rhamnan Sulfate (100 mg)
  - Antarctic Krill Oil (1,000 - 2,000 mg)
  - Olive Leaf Extract (500 mg, 20% Oleuropein)
  - Benfotiamine (150 mg) + L-Carnosine (500 mg) + Pyridoxamine / P-5-P (50 mg)
  - L-Ergothioneine (25 mg)

### 16:00 - 16:30 | Functional Powder Vehicle: "One Smoothie Per Day" (Module 37)
- Ingested in the late afternoon focus window.
- **Carbohydrate-only, zero-dairy, zero-collagen powder vehicle:**
  - 1 cup frozen organic wild blueberries (Anthocyanin/polyphenol dense)
  - 1 cup unsweetened coconut water or RO water + splash of lemon juice
  - Chondroitin Sulfate (1,200 mg powder)
  - Amla Fruit Extract Powder (1,000 mg)
  - Taurine Powder (3,000 - 5,000 mg)
  - Glycine Powder (3,000 - 5,000 mg)
  - Organic Greens Blend (Spirulina / Chlorella / Barley Grass: 5 g)
  - Organic Agaricus Blazei Murill Mushroom Extract (1,000 mg)
  - Creatine Monohydrate (5 g)

### 17:30 - 18:45 | Thermal Hormesis & Cellular Stimulation Window (Modules 28, 30)
- **Dispensing:** **Pillbox Slot 3 (Pre-Hormesis Pouch)** taken 60 min prior:
  - Sodium Chloride / Electrolyte cap (1,000 mg)
  - Quercetin Phytosome (250 mg) + EGCG (200 mg)
- **Finnish Sauna Protocol (Module 28):** 80-90°C (176-194°F) for 20-30 minutes with intermittent löyly (steam). Triggers HSP70 molecular chaperone induction and plasma volume expansion.
- **Photobiomodulation (Module 30):** Full-body red/NIR panel (660nm & 850nm) at 30-50 mW/cm² for 10-15 minutes to charge cytochrome c oxidase.

### 19:15 - 20:00 | Evening Dinner (Meal 2)
- Lighter meal: cruciferous vegetables (steamed broccoli, Brussels sprouts), fermented vegetables (kimchi, sauerkraut), extra virgin olive oil, and clean protein (tofu, tempeh, or fish).
- If carbohydrates are present, take secondary Acarbose (25 mg).

### 21:00 - 21:30 | Nighttime Kitchen Treat: Evening Collagen Mugcake (Module 37)
- Low-temperature microwave functional cake:
  - 15 g Hydrolyzed Collagen Peptides
  - 1 tbsp raw unsweetened cacao powder (flavanols)
  - 1 tbsp almond flour or oat fiber
  - 1 pinch baking powder + Ceylon cinnamon
  - 3 tbsp unsweetened almond milk or water
  - Sweeten with pure stevia or monkfruit
  - Microwave on medium-low for 45-60 seconds. Provides glycine-rich somnogenic neurotransmission while delivering structural peptides during slow-wave sleep.

### 21:30 - 22:30 | Nighttime Down-Regulation & Sleep Ingestion
- Dim all lights; put on blue-blocking glasses.
- **Dispensing:** **Pillbox Slot 4 (Evening Bedtime)**:
  - Magnesium L-Threonate / Bisglycinate (200-400 mg elemental)
  - L-Theanine (200 mg)
  - Apigenin (50 mg)
  - Inositol (2,000 mg)
  - Taurine (1,000 - 2,000 mg, if not fully consumed in smoothie)
- **Subcutaneous Peptide Injection (Mon-Fri Nights, Module 19):** Ipamorelin (200 mcg) + CJC-1295 no-DAC (100 mcg) injected subQ into abdominal adipose 60 minutes after mugcake on an empty stomach.
- **Sleep Hardware (Module 31):** Apply gentle 3M micropore mouth tape. Activate transcutaneous auricular vagus nerve stimulation (taVNS) ear clip (25 Hz, 200 µs pulse) for 20-30 minutes. Bedroom temperature set to 66°F (19°C).

---
""")

    # 3. Section IV: The Physical Pillbox Dispensing Matrix
    doc.append("""# SECTION IV: THE PHYSICAL PILLBOX DISPENSING MATRIX & STORAGE GUIDE
*A complete 1-page physical adherence matrix mapping every oral compound to standard 7-day 4-compartment organizers.*

""" + pillbox_content + """

---
""")

    # 4. Section V: Precision Longevity Kitchen & Powder Vehicles (Module 37)
    # We load Module 37 directly
    m37_path = os.path.join(INTERVENTIONS_DIR, "37_Longevity_Nutrition_Recipes_and_Powders.md")
    if os.path.exists(m37_path):
        doc.append("""# SECTION V: PRECISION NUTRITION, FUNCTIONAL RECIPES & POWDER VEHICLES (MODULE 37)
""" + load_file(m37_path) + """

---
""")

    # 5. Section VI: Athletic Performance Architecture (Module 38)
    m38_path = os.path.join(INTERVENTIONS_DIR, "38_Athletic_Performance_BMT_Triphasic_Sprinting.md")
    if os.path.exists(m38_path):
        doc.append("""# SECTION VI: ATHLETIC PERFORMANCE ARCHITECTURE: BMT, DYNAMIC ELASTICITY & SPRINTING (MODULE 38)
""" + load_file(m38_path) + """

---
""")

    # 6. Section VII: Valter Longo Fasting Mimicking Diet (Module 39)
    m39_path = os.path.join(INTERVENTIONS_DIR, "39_Longo_Fasting_Mimicking_Diet_FMD.md")
    if os.path.exists(m39_path):
        doc.append("""# SECTION VII: VALTER LONGO FASTING MIMICKING DIET (FMD) (MODULE 39)
""" + load_file(m39_path) + """

---
""")

    # 7. Section VIII: The Infradian Master Architecture (Module 40)
    m40_path = os.path.join(INTERVENTIONS_DIR, "40_Infradian_Pulsed_Interventions_Cadence.md")
    if os.path.exists(m40_path):
        doc.append("""# SECTION VIII: THE INFRADIAN MASTER ARCHITECTURE: PERIODIC & PULSED PROTOCOLS (MODULE 40)
""" + load_file(m40_path) + """

---
""")

    # 8. Section IX: The Complete 42-Module Interventions Ledger (Modules 01 - 42)
    doc.append("""# SECTION IX: THE UNABRIDGED 42-MODULE INTERVENTIONS LEDGER

This ledger contains the exhaustive biophysical, pharmacokinetic, clinical, and surveillance details for all 42 active protocol interventions.

""")

    for fpath in interv_files:
        fname = os.path.basename(fpath)
        # Avoid duplicating 37, 38, 39, 40 since we already have dedicated sections above, or include them with clean subheadings
        m_num = int(re.match(r"(\d+)_", fname).group(1))
        content = load_file(fpath)
        doc.append(f"""## MODULE {m_num:02d}: {fname.replace('.md', '').replace('_', ' ')}
{content}

---
""")

    # 9. Section X: The Epistemic Graveyard & Retired Interventions
    doc.append("""# SECTION X: THE EPISTEMIC GRAVEYARD (RETIRED & DEPRECATED INTERVENTIONS)

Honest longevity requires ruthless termination of hypotheses when empirical human trials or biophysical realities contradict theoretical enthusiasm. The following interventions were tested, audited, and permanently retired from the active Kenaley Protocol:

### RET-01: Chronic Daily Metformin in Resistance-Trained Lifters
- **Historical Thesis:** AMPK activation, complex I inhibition, suppression of hepatic gluconeogenesis, and observational epidemiological associations with reduced cancer and mortality in diabetic cohorts.
- **Empirical Cause for Termination:** The landmark **MASTERS Trial (Walton et al., Aging Cell 2019)** demonstrated that chronic metformin administration in healthy older adults blunted skeletal muscle hypertrophic response to resistance training by 30-50% and impaired mitochondrial respiration in healthy muscle tissue.
- **Biophysical Mechanism of Failure:** Chronic complex I inhibition creates an ongoing cellular energetic deficit that attenuates post-exercise mTORC1 activation, satellite cell proliferation, and myofibrillar protein synthesis. In a lean, non-diabetic individual performing heavy resistance training (BMT), metformin impairs the very organ system (skeletal muscle) most strongly correlated with all-cause mortality resistance.
- **V5 Replacement:** Replaced with **Acarbose (Module 01)**, which delivers superior mammalian lifespan extension (+22% NIA ITP) via cecal starch shunting and short-chain fatty acid (butyrate) production *without* entering systemic circulation or blunting muscular hypertrophy.

### RET-02: Dasatinib + Quercetin (D+Q) Senolytic Regimen
- **Historical Thesis:** Broad-spectrum senolytic cocktail combining the tyrosine kinase inhibitor dasatinib (targeting senescent adipocyte/endothelial cells) and the polyphenol quercetin (targeting senescent endothelial/epithelial cells).
- **Empirical Cause for Termination:** Significant off-target hematological and vascular toxicities associated with dasatinib, including risks of pleural effusion, pulmonary arterial hypertension, thrombocytopenia, and systemic immunosuppression.
- **Biophysical Mechanism of Failure:** Dasatinib exhibits low selectivity, inhibiting multiple BCR-ABL, SRC, and c-KIT kinases in healthy hematopoietic stem and progenitor cells. The therapeutic window in non-diseased individuals seeking preventative longevity is unacceptably narrow.
- **V5 Replacement:** Transitioned to **Mayo Pulsed Fisetin (Module 14)**. Fisetin demonstrates superior senolytic potency against senescent human fibroblasts, osteoclasts, and vascular cells with zero hematological toxicity, negligible off-target kinase inhibition, and a benign safety profile during intermittent 2-day monthly pulses.

### RET-03: Continuous C60 Fullerene in Olive Oil (Baati Protocol)
- **Historical Thesis:** Baati et al. (Biomaterials 2012) reported an unprecedented +90% lifespan extension in Wistar rats administered C60 dissolved in extra virgin olive oil, hypothesized to act as a reusable catalytic super-antioxidant inside the mitochondrial inner membrane.
- **Empirical Cause for Termination:** Independent, rigorous replication attempts (Grohn et al., 2021) completely failed to replicate any lifespan extension. Furthermore, unfunctionalized C60 particles demonstrate batch-to-batch chemical heterogeneity, phototoxicity upon exposure to ambient light (generating toxic epoxides and reactive oxygen species), and indefinite tissue bioaccumulation with unknown clearance pathways in humans.
- **Biophysical Mechanism of Failure:** Photolyzed C60 forms cytotoxic degradation products that induce membrane permeabilization and lipid peroxidation rather than preventing it.
- **V5 Replacement:** Permanently retired. Inner mitochondrial membrane cardiolipin integrity is achieved via **SS-31 (Elamipretide, Module 04)** and **Polyunsaturated Cardiolipin Precursors (DLPC, Module 35)**.

### RET-04: Supraphysiological TRT & rhGH
- **Historical Thesis:** Maintaining supra-youthful anabolic hormone concentrations (Testosterone > 1200 ng/dL, IGF-1 > 350 ng/mL) to maximize muscle mass and lipolysis.
- **Empirical Cause for Termination:** Supraphysiological exogenous testosterone causes complete hypothalamic-pituitary-gonadal (HPG) axis shutdown, testicular atrophy, severe hematocrit elevation (>54%), secondary polycythemia, and elevated thrombotic cardiovascular risk. Continuous recombinant human growth hormone (rhGH) drives persistent hyperinsulinemia, insulin resistance, accelerated somatic cellular senescence, and elevated oncogenic transformation risk.
- **V5 Replacement:** Replaced by **Endocrine Axis Preservation**: **Microdose Trans-Enclomiphene (Module 17)** to stimulate endogenous LH/FSH and testicular testosterone synthesis without axis shutdown, paired with **Pulsatile Nocturnal GHRH/GHRP Secretagogues (Ipamorelin/CJC-1295, Module 19)** to mimic natural physiological youthful pulses without inducing hyperinsulinemia or shutting down pituitary somatotrophs.

### RET-05: Chronic High-Dose Non-Selective Antioxidants (Vitamins C & E Post-Workout)
- **Historical Thesis:** Scavenging all exercise-induced free radicals with massive doses of oral Vitamin C (1000+ mg) and Vitamin E (400+ IU) to minimize oxidative muscle damage and fatigue.
- **Empirical Cause for Termination:** Landmark trials (Ristow et al., PNAS 2009; Paulsen et al., J Physiol 2014) conclusively proved that chronic high-dose antioxidants blunt exercise-induced mitochondrial biogenesis, block PGC-1alpha upregulation, impair insulin sensitivity improvements, and prevent skeletal muscle adaptation.
- **Biophysical Mechanism of Failure:** Exercise-induced reactive oxygen species (ROS) are critical hormetic signaling molecules that activate the Nrf2-ARE antioxidant pathway, PGC-1alpha transcription, and endogenous SOD2/catalase expression. Neutralizing this physiological signal prevents the body from building its own durable endogenous defense systems.
- **V5 Replacement:** Strict timing separation. Oral Vitamin C is limited to physiological co-factor doses (500 mg with morning collagen broth or Ca-AKG) and kept completely separate from post-workout adaptation windows. Cellular protection is achieved via targeted endogenous defense inducers (**PQQ Module 05**, **Sulforaphane**, **Finnish Sauna HSP70 Module 28**).

---
""")

    # 10. Section XI: Safety, Drug-Drug Interaction & Kinetic Collision Matrix
    doc.append("""# SECTION XI: COMPREHENSIVE PHARMACOLOGICAL SAFETY & COLLISION MATRIX

The Kenaley Protocol enforces the following immutable pharmacological safety rules:

| Primary Compound | Interacting Agent | Potential Collision / Failure Mode | Mandatory Operational Mitigation |
| :--- | :--- | :--- | :--- |
| **Microdose Tadalafil (INT-10)** | Organic Nitrates (Nitroglycerin, Isosorbide) | Catastrophic, potentially fatal systemic hypotension via unchecked cGMP accumulation. | **ABSOLUTE CONTRAINDICATION.** Never co-administer tadalafil with prescription nitrates. |
| **Sublingual Selegiline (INT-22)** | Aged / Fermented Cheeses, High-Tyramine Foods, SSRIs / SNRIs | Hypertensive crisis ("Cheese Effect") or Serotonin Syndrome. | Maintain sub-microdose threshold (0.25 mg Mon/Wed/Fri sublingually). At this dose, MAO-A in the gut and liver is completely spared (>98% uninhibited), eliminating the tyramine pressor response. Avoid synthetic sympathomimetics and high-dose SSRIs. |
| **Acarbose (INT-01)** | Pure Ketogenic / Zero-Carb Meal | Complete lack of enzymatic substrate; gastrointestinal discomfort without biological efficacy. | Take Acarbose ONLY with meals containing >= 20g complex starches. Omit on fasted or pure fat/protein meals. |
| **Mayo Pulsed Fisetin (INT-14)** | Continuous Administration | Chronic clearance of necessary senescent-like remodeling cells (e.g., wound healing, tissue repair); potential blunting of endogenous stem cell signaling. | Enforce strict pulsed cadence: 2 consecutive days per month only (20 mg/kg/day). Never dose continuously. |
| **Turnbuckle Fission Cycle (INT-03)** | Long-Term Uncycled Use | Chronic mitochondrial fragmentation, severe ATP depletion, impaired muscle recovery, cellular crisis. | Enforce strict 4-day quarterly pulse: 4 days of fission induction immediately followed by high-dose fusion and cardiolipin rebuilding (SS-31, DLPC, PQQ). |
| **Exemestane (INT-18)** | Excessive Dosing without Lab Surveillance | Total estradiol crash (< 10 pg/mL), leading to accelerated arterial stiffness, loss of bone mineral density, joint pain, lipid dysregulation, and severe depressive symptoms. | Microdose only (6.25 mg twice weekly or as needed). Monitor serum ultrasensitive Estradiol quarterly; maintain target range 20 - 30 pg/mL. Discontinue immediately if E2 < 15 pg/mL. |
| **Enclomiphene (INT-17)** | Long-term use without Hematocrit Monitoring | Secondary erythrocytosis / elevated hematocrit (> 52%), increasing blood viscosity and thrombotic risk. | Quarterly CBC surveillance. Titrate down or conduct therapeutic phlebotomy / plasmapheresis if hematocrit exceeds 52%. |

---
""")

    # 11. Section XII: Biomarker Surveillance Targets & Lab Frequency
    doc.append("""# SECTION XII: QUANTIFIED SURVEILLANCE BIOMARKER TARGETS & LABORATORY SCHEDULE

### 12.1 The Clinical Target Matrix
Every active bet must be justified against objective, quantified biomarker surveillance:

| Physiological Domain | Biomarker | Standard Clinical Range | **Kenaley Protocol v5.0 Target Range** | Clinical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Cardiovascular Risk** | **Apolipoprotein B (ApoB)** | 60 - 130 mg/dL | **< 35 mg/dL** | Eliminates lifetime atherogenic particle exposure; prevents plaque initiation. |
| **Systemic Inflammation** | **High-Sensitivity CRP (hs-CRP)** | 0.0 - 3.0 mg/L | **< 0.30 mg/L** | Suppresses microvascular endothelial inflammation and vascular senescence. |
| **Glucose Regulation** | **Fasting Insulin** | 2.6 - 24.9 µIU/mL | **2.0 - 4.5 µIU/mL** | Minimizes chronic hyperinsulinemia and promotes basal autophagy. |
| **Glycemic Control** | **HbA1c** | 4.0 - 5.6 % | **4.6 - 5.1 %** | Prevents advanced glycation end-product (AGE) formation without hypoglycemia. |
| **Insulin Sensitivity** | **HOMA-IR** | < 2.0 | **< 0.80** | Pristine skeletal muscle and hepatic insulin sensitivity. |
| **Renal Function** | **Cystatin C** | 0.62 - 1.15 mg/L | **0.65 - 0.85 mg/L** | Muscle-mass-independent gold standard for glomerular filtration rate. |
| **Endocrine / Androgens** | **Total Testosterone** | 300 - 1000 ng/dL | **700 - 950 ng/dL** | Youthful androgenic signaling, bone density, and neuroprotection. |
| **Endocrine / Androgens** | **Free Testosterone** | 35 - 155 pg/mL | **120 - 180 pg/mL** | Bioavailable androgen for skeletal muscle and libido. |
| **Endocrine / Estrogens** | **Estradiol (Ultrasensitive)**| 10 - 40 pg/mL | **20 - 30 pg/mL** | Endothelial nitric oxide stimulation and bone mineral preservation. |
| **Thyroid Architecture** | **Free T3 / Free T4** | 2.0 - 4.4 pg/mL | **3.2 - 3.8 pg/mL** | Optimal basal metabolic rate and mitochondrial oxygen consumption. |
| **Biological Aging** | **DunedinPACE Clock** | 0.60 - 1.40 | **< 0.45** | Top-tier pace of biological aging deceleration (Rejuvenation Olympics standard). |

### 12.2 Laboratory Surveillance Frequency
1. **Quarterly Blood Panel (Every 90 Days):**
   - Comprehensive Metabolic Panel (CMP) + Complete Blood Count (CBC with differential)
   - Advanced Lipid Panel (ApoB, LDL-P, Lp(a), Triglycerides, HDL-C)
   - Endocrine Profile: Total & Free Testosterone (LC/MS), Ultrasensitive Estradiol, SHBG, LH, FSH, IGF-1
   - Glycemic Panel: Fasting Glucose, Fasting Insulin, HbA1c
   - Inflammatory / Renal: hs-CRP, Cystatin C, Uric Acid, Homocysteine, Ferritin
2. **Semiannual Epigenetic Clock (Every 6 Months):**
   - DunedinPACE, OMICmAge, PhenoAge, Horvath DNA methylation saliva/blood test.
3. **Annual Diagnostic Imaging & Screening:**
   - Multi-cancer early detection liquid biopsy (e.g., Galleri test).
   - Low-dose coronary artery calcium (CAC) CT scan or Cleerly CCTA plaque analysis.
   - Whole-body diffusion-weighted MRI (e.g., Prenuvo / Ezra) for early structural pathology detection.
   - Carotid intima-media thickness (CIMT) ultrasound with arterial stiffness pulse wave velocity.

---

# SECTION XIII: CONCLUSION & SUMMARY DIRECTIVE
The Kenaley Longevity Protocol v5.0 represents a complete, mathematically coherent, biophysically grounded human longevity blueprint. By integrating daily circadian chronobiology, athletic dynamic elasticity (BMT), precision functional nutrition (RS3, collagen broth, powder vehicles), and periodic infradian autophagic/senolytic pulses, it provides a comprehensive system for achieving the absolute physiological frontier of human healthspan.
""")

    full_text = "\n".join(doc)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    root_out_path = os.path.join(ROOT_DIR, "KENALEY_LONGEVITY_V5_MASTER_LLM.md")
    with open(root_out_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    print(f"Lossless Master Markdown successfully written to: {OUT_PATH} and {root_out_path}")
    print(f"Total size: {len(full_text)} characters, {len(full_text.splitlines())} lines.")

if __name__ == "__main__":
    main()
