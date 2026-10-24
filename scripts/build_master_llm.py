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
> 4. **The Physical 3-Slot Pillbox Dispensing Matrix + Pulsed Training Pouches & Lab Fridge Storage**
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

## 1.4 The Pareto Frontier: Non-Consensus Alpha (High-EV Architectural Innovations)

The **Kenaley Longevity Protocol v5.0** transcends standard biohacking by shifting focus from single-target supplement stacking to **stoichiometric rate-limiters, biophysical membrane geometry, and temporal phase separation**. While conventional protocols blindly push NAD+ or chronic AMPK activation, your highest-expected-value (EV) innovations lie where you solve multi-variable kinetic traps that cause standard interventions to stall or backfire:

### 1. The PEMT–Tafazzin–SS-31 Cardiolipin Triad (Modules 04 & 35)
Most mitochondrial stacks dump electrons into a leaky electron transport chain via CoQ10 or NMN without fixing the physical scaffolding of the inner mitochondrial membrane (IMM):
* **Substrate-Level Acyl Remodeling:** Supplying 1,2-dilinoleoylphosphatidylcholine (DLPC, $18:2/18:2\text{-PC}$) provides the exact linoleoyl donor required by the transacylase **Tafazzin (TAZ)** to remodel monolysocardiolipin into mature **tetralinoleoyl cardiolipin (\text{L}_4\text{CL})**, preventing pathological **ALCAT1**-driven substitution of peroxidizable DHA chains into the IMM.
* **Solving the Three-Way Methylation Collision:** Recognizing that synthesizing phosphatidylcholine via **PEMT** consumes 3 molecules of SAMe (producing 3 molecules of SAH, which competitively inhibits both PEMT and TET/DNMT epigenetic maintenance) and offsetting this by offloading **GAMT** via exogenous Creatine (sparing ~45% of systemic SAMe) plus TMG is first-rate stoichiometric engineering.
* **Electrostatic Locking:** Pulsing **SS-31** to form salt bridges with the dianionic phosphate headgroups of that newly remodeled $\text{L}_4\text{CL}$ sterically blocks the rupture of the $\text{Fe-Met80}$ coordination bond in Cytochrome $c$, preventing its conversion into a cardiolipin-specific peroxidase.

### 2. Commercial Plasmapheresis + Endogenous Cys34-SH Mercaptalbumin Synthesis (Modules 15 & 16)
Clinical Therapeutic Plasma Exchange (TPE) with 5% bottled human serum albumin costs $5,000+ per session, whereas utilizing commercial plasma donation centers is cash-flow positive and removes 800 mL of aged proteome ($\text{TGF-}\beta 1$, $\text{GDF15}$, $\text{CCL11}$, $\beta_2\text{-microglobulin}$, and circulating PFAS/microplastics).
* **The Unspoken Biochemical Alpha:** Bottled pharmaceutical 5% albumin used in clinical TPE undergoes heavy oxidation during manufacturing and storage, meaning its catalytic **$\text{Cys34}$ free thiol** is largely oxidized into non-mercaptalbumin (sulfinic/sulfonic states). By replacing volume with saline and immediately forcing the liver to synthesize 40–50 g of *de novo* albumin under a heavy **GlyNAC + EAA + Silymarin** load, your newly secreted albumin enters circulation with $>75\%$ reduced **$\text{Cys34-SH}$ mercaptalbumin**—the single most abundant extracellular free-radical scavenger in human plasma. You achieve a superior redox outcome compared to clinical TPE for pennies.

### 3. Unblocking the Hepatic Kupffer Cell EP2 -> GYS1 Efferocytosis Trap (Module 42)
Translating the 2026 Andreasson Lab (*Science*) hepatic tissue-resident macrophage (TRM) discovery into an outpatient stack avoids the classic anti-inflammatory trap:
* **Bypassing the NSAID Paradox:** Blunt COX-2 inhibition lowers $\text{PGE}_2$ but wipes out Specialized Pro-resolving Mediators (SPMs: lipoxins/resolvins), arresting the engulfment phase of efferocytosis. Using **AKBA (Boswellia) + Curcumin** to selectively inhibit terminal **$\text{mPGES-1}$** while loading **EPA/DHA + SPMs** drops $\text{PGE}_2$ tone without starving GPR32/ALX resolution receptors.
* **Reversing Glycogen Sequestration:** Because $\text{PGE}_2\text{--}\text{EP2}$ signaling inhibits $\text{GSK3}\beta$ and hyper-activates Glycogen Synthase 1 ($\text{GYS1}$)—trapping glucose in inert glycogen so Kupffer cells lack the glycolytic ATP required for actin-mediated phagocytosis of $\text{CXCR4}^{\text{hi}}$ senescent neutrophils—deploying **C3G** to drive AMPK-mediated inhibitory phosphorylation of $\text{GYS1}$ at Ser8 while activating **$\text{LXR}\alpha \to \text{MerTK}$** ("eat-me" receptors) and scavenging MPO-derived $\text{HOCl}$ with **Taurine** attacks the exact molecular bottleneck.

### 4. The Anabolic-Butyrogenic Cecal Starch Shunt (Modules 01 & 37)
Strict ketogenic or low-carb diets impair explosive glycolytic Rate of Force Development (RFD) and thyroid conversion, while high-carb diets drive methylglyoxal (MGO) and **glucosepane** ECM crosslinks.
* Combining high-pressure gelatinized, $4^\circ\text{C}$-retrograded **RS3 resistant starch** (crystalline $\alpha\text{-(1}\to\text{4)}$-D-glucan double helices) with first-bite **Acarbose** and brush-border SGLT1/GLUT2 inhibition (**C3G**) solves this trade-off. You support athletic glycogen repletion while shunting $>60\%$ of the carbohydrate mass to the distal ileum and cecum, converting a potential glycemic spike into a massive wave of Class I/II HDAC-inhibiting **butyrate** and endogenous L-cell GLP-1.

### 5. Anatomical Decoupling of the Oral Microbiome (Module 34)
Recognizing that 4 of the 19 physiological slopes training the **DunedinPACE** clock (~21% of total clock weight: periodontal attachment loss, caries, hs-CRP, and neutrophil/WBC count) stem directly from *P. gingivalis* gingipains and subgingival endotoxemia is a massive analytical catch.
* Antiseptic mouthwashes lower hs-CRP from gingivitis but wipe out lingual facultative anaerobes (*Veillonella atypica*, *Rothia mucilaginosa*), destroying the enterosalivary $\text{NO}_3^- \to \text{NO}_2^- \to \text{NO}$ pathway and starving **Microdose Tadalafil (Module 10)** of upstream cGMP. Using a Pik Pocket to restrict **0.10% NaOCl** strictly to subgingival pockets while seeding the tongue dorsum with ***S. salivarius* K12/M18** captures both the epigenetic clock benefit and vascular eNOS/sGC synergy.

### 6. De-Risked "Turnbuckle" Niche Expansion & CHIP Gatekeeping (Modules 03, 41 & 42)
The original community Turnbuckle protocol was biochemically reckless. The v5.0 rewrite fixes three critical failure modes:
* Replacing 100 mg **Sulforaphane** (which hyper-activates Keap1/NRF2, represses Notch1, and forces premature asymmetric differentiation that exhausts neural and hematopoietic stem cell pools) with **C18:0 Stearic Acid / GMS** to covalently stearoylate Transferrin Receptor 1 (TfR1), inhibit JNK, and stabilize MFN1/2 physiologically.
* Excising **D-Ribose** (which glycates proteins 50–100$\times$ faster than glucose) and phototoxic **$\text{C}_{60}$ fullerenes**.
* **Sequencing Senolysis & PAI-1 Inhibition Before Mobilization:** Mobilizing $\text{CD34}^+$ progenitors with **Fucoidan** or G-CSF in an inflamed, senescent bone marrow niche preferentially expands pre-leukemic **CHIP** clones (*DNMT3A*, *TET2*, *ASXL1*) that thrive under NF-$\kappa$B signaling. Enforcing an NGS CHIP gatekeeper ($VAF < 2\%$) and running **Mayo Fisetin + PCC1 (Module 14)** and **TM5614 oral PAI-1 inhibition (Module 41)** *prior* to mobilization is the only safe way to execute endogenous stem cell expansion.


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

The protocol organizes all pharmacological, nutritional, and physical interventions into strict circadian windows to eliminate kinetic collisions, prevent receptor cross-tolerance, and align with natural physiological oscillators.

---

### The Fundamental Kinetic Conflict: The 4-Hour Hormetic ROS Collision
A foundational biophysical rule of the Kenaley Architecture is:
> **STRICTLY ZERO ANTIOXIDANTS (NAC, Vitamin C, Amla, Astaxanthin, PQQ, or high-dose polyphenols) within 4 hours before or after Sprinting (Module 38), Finnish Sauna (Module 28), or HBOT (Module 29).**

Endogenous mitochondrial reactive oxygen species (superoxide, $\text{H}_2\text{O}_2$) generated during mechanical or thermal stress are required signaling messengers that oxidize Keap1 to stabilize **Nrf2** and stabilize **HIF-1$\alpha$**. 

Because the **Master Blueberry Powder Smoothie (Module 37)** delivers an extraordinarily dense reducing payload (**$1.0\text{ g}$ pure NAC + $2.5\text{ g}$ Amla + $330\text{ mg}$ C3G + Wild Blueberries**), consuming it between a midday training session and an afternoon sauna completely quenches the hormetic adaptation.

To remain 100% collision-free, execute one of the two standardized daily chronobiological tracks:

---

### 🏃 TRACK A: MIDDAY TRAINING + IMMEDIATE POST-WORKOUT THERMAL HORMESIS (12:00 – 14:00 HORMETIC BLOCK)
*Optimized for professionals who bundle athletic training directly with Finnish sauna, Far-Infrared (FIR) sauna, or Hot Water Immersion (HWI) in a single early-afternoon block.*

* **06:30 - 07:00 | Circadian Awakening & Cortisol Awakening Surge:**
  - **Photobiology:** Step outside for 10-15 minutes of direct solar photon exposure to reset the suprachiasmatic nucleus (SCN).
  - **Hydration:** 20-24 oz (600-750 mL) purified RO water with Celtic sea salt / potassium bicarbonate.
  - **Dispensing:** **Pillbox Slot 1 (AM Fasted)** swallowed with water:
    - Urolithin A (1,000 mg) — Fasted PINK1/Parkin mitophagy & HSC rejuvenation
    - Calcium-AKG (1,000 mg) — TET1–3 DNA demethylation co-substrate & systemic IL-10 surge *(or powder in water/smoothie)*
    - Liposomal Vitamin C (500 mg) — Reduces active-site $\text{Fe}^{3+} \to \text{Fe}^{2+}$ for TET enzymes
    - Microdose Tadalafil (2.5 - 5.0 mg) — Endothelial cGMP / PKG1 signaling & renal eGFR
    - Low-Dose Lithium Orotate (5 mg elemental) — GSK-3$\beta$ inhibition & hippocampal BDNF preservation
    *(Note: Spermidine capsules are retired in favor of the colonic bioreactor; Cat's Claw AC-11 is retired due to C3G SIRT6-PARP1 redundancy; Apigenin is moved to Slot 3 PM).*
  - **Sublingual / Mon-Wed-Fri Only:** Selegiline (0.25 mg sublingual). *Allow to absorb under tongue for 5 minutes; do not swallow whole.*
  - **Oral Protocol (Module 34):** Tongue scraping followed by remineralizing nano-hydroxyapatite brushing. Subgingival 0.10% NaOCl via Pik Pocket tip 2x/week.
* **07:00 - 11:30 | Fasted Deep Work & Cognitive Focus Window:**
  - Maximum cognitive clarity period powered by high fasted dopamine and low insulin. Pure black coffee or ceremonial green tea.
* **11:30 | Pre-Workout Joint & Fascial Priming (30 min prior):**
  - Drink the **Savory Pre-Workout Broth** (Module 37: 15g Hydrolyzed Collagen Peptides + 200–500 mg HMW-HA + 1/4 tsp salt + Zinc Carnosine). *(Hold high-dose Vitamin C or keep to <=250 mg so workout ROS is unhindered).*
* **12:00 - 14:00 | High-Intensity Athletic Training & Thermal Hormesis Block:**
  - **12:00 - 13:15 (Module 38):** Dynamic fascial warmup $\to$ high-load eccentric squats/plyos (Day A) or max-velocity sprints/upper work (Day B).
  - **13:15 (Thermal Priming):** Take **Pre-Hormesis Training Pouch (Module 27)**: Selbex (Teprenone / GGA 100 mg) + 1,000 mg electrolyte salt. *(No inorganic nitrate pre-heat).*
  - **13:30 - 14:00 (Module 28):** Thermal Hormesis:
    - *Option 1 (Finnish Dry Sauna):* 80–90°C for 20–25 minutes.
    - *Option 2 (Far-Infrared FIR Sauna):* 55–65°C for 30–45 minutes.
    - *Option 3 (Hot Water Immersion HWI):* 40–42°C (104–108°F) bath up to neck for 20–30 minutes.
* **14:15 - 15:00 | Post-Workout Nutrition & Main Refuel (Meal 1):**
  - High-protein lean meal + Pressure-Cooked Retrograded RS3 Resistant Starch (Module 37).
  - **Pillbox Slot 2 (Midday / Meal 1):** Acarbose (25–50 mg with first forkful), Bempedoic Acid + Ezetimibe, Citrus Bergamot, Vitamin K2 MK-7 + D3 + Retinol, Kyolic Aged Garlic, Rhamnan Sulfate, Krill Oil, Olive Leaf Extract, Benfotiamine + Carnosine + Pyridoxamine, L-Ergothioneine.
* **15:00 - 18:15 | Afternoon Deep Work & Digest Window:**
  - 4-hour post-workout/post-thermal Nrf2 and HSP70 transcriptional signaling cascades run without antioxidant interference.
* **18:15 - 18:45 | THE SMOOTHIE WINDOW (>4 Hours Post-Thermal) & Dinner (Meal 2):**
  - **Consume the Master Blueberry Powder Smoothie (Module 37):** 1.25 cups frozen wild blueberries + lemon juice + 25.5g dry payload (Glycine 7.5g, Creatine 5g, Greens 5g, Amla 2.5g, Taurine 1.5g, TMG 1.5g, Chondroitin 1.2g, NAC 1.0g, Agaricus 1.0g, C3G 330mg).
  - Floods the liver with GlyNAC, Taurine, and C3G right as restorative parasympathetic tone begins. C3G simultaneously blocks brush-border SGLT1/GLUT2 for Meal 2 carbs.
  - Light dinner of steamed cruciferous vegetables, extra virgin olive oil, and clean protein.
* **20:45 - 21:15 | Evening Collagen Mugcake (Module 37):**
  - 15g Collagen + Casein + Cacao + Coconut Flour (60 sec microwave).
* **21:30 - 22:30 | Nighttime Down-Regulation, Alkalinizing Drink & Sleep Ingestion:**
  - Dim lights, blue-blockers on.
  - **Recipe 5: Nocturnal Alkalinizing Sleep Cocktail:** 1/2 tsp (2.0–2.5g) Sodium Bicarbonate + 2.0–3.0g Myo-Inositol dissolved in 4–6 oz warm water.
  - **Pillbox Slot 3 (Evening Bedtime):** DLPC (1.2–2.4g), L-Theanine (200 mg), Apigenin (50 mg), Kyolic SAC (600 mg), Chebulic+Rosmarinic acid, Melatonin microdose (0.3–1.0 mg), Mg L-Threonate (300–400 mg). *(PEA excised; TMG consolidated to smoothie).*
  - **Pre-Bed Oral Probiotic (Module 34):** Dissolve 1 *S. salivarius* K12/M18 oral probiotic lozenge slowly on the tongue.
  - **Topical Dermatology (Module 32):** Niacinamide 5% followed by Tretinoin 0.05% cream.
  - **Sleep Hardware (Module 31):** 3M Micropore mouth tape + 15 min taVNS ear clip (25 Hz left tragus). Cool dark room (65–68°F).

---

### 🌅 TRACK B: LATE-AFTERNOON TRAINING + THERMAL HORMESIS (16:30 – 18:30 HORMETIC BLOCK)
*Optimized for individuals who train in the late afternoon/early evening.*

* **06:30 - 10:00 | Fasted Deep Work & Slot 1 AM Pills:**
  - Solar exposure + hydration + Slot 1 AM pills + sublingual Selegiline (M/W/F).
* **10:30 - 11:00 | THE SMOOTHIE WINDOW (>5.5 Hours Pre-Training):**
  - Break morning fast with the **Master Blueberry Powder Smoothie (Module 37)**.
  - *Why this works:* Being strictly fat-free and fiber-dispersed, gastric transit completes within 45–60 minutes and plasma NAC free-thiols peak and clear well before 16:30, leaving cellular redox unbuffered for workout ROS.
* **12:30 - 13:15 | Main Refuel (Meal 1):**
  - Main RS3 starch + lean protein meal + Pillbox Slot 2.
* **15:30 | Pre-Workout Joint Priming & Thermal Priming (60 min prior):**
  - Savory Collagen Broth (15g Collagen + 200–500 mg HMW-HA) + Pre-Hormesis Training Pouch (Selbex 100 mg + Electrolytes).
* **16:30 - 18:30 | High-Intensity Athletic Training & Thermal Hormesis Block:**
  - Module 38 BMT Sprints/Lifting $\to$ Module 28 Finnish Sauna, Far-Infrared Sauna, or Hot Water Immersion.
* **19:15 - 20:00 | Evening Dinner (Meal 2):**
  - Whole-food dinner + secondary Acarbose if carbs present.
* **20:45 - 22:30 | Mugcake, Sleep Cocktail, Slot 3 Bedtime Stack & Sleep Hardware:**
  - Mugcake at 20:45 $\to$ Recipe 5 Alkalinizing Cocktail (Bicarb + Myo-Inositol) & Slot 3 Bedtime pills at 21:30 $\to$ *S. salivarius* lozenge $\to$ Topical PM Tretinoin/Niacinamide $\to$ Mouth tape + taVNS.

---
# SECTION IV: THE PHYSICAL PILLBOX DISPENSING MATRIX & STORAGE GUIDE
*A complete 1-page physical adherence matrix mapping every oral compound to standard 7-day 3-compartment organizers plus pulsed training pouches.*

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
    doc.append("""
### RET-06: Cat's Claw / AC-11 (Aqueous Uncaria tomentosa Extract)
- **Historical Thesis:** Standardized carboxy alkyl esters (CAEs) were claimed to upregulate PARP-1 activity and enhance nucleotide excision repair (NER) of DNA lesions.
- **Empirical Cause for Termination:** Heavy reliance on small early-2000s commercial pilot studies (Sheng/Pero); the exact active pharmacokinetic CAE monomer in human plasma remains poorly characterized.
- **Biophysical Mechanism of Failure & Redundancy:** Completely superseded by **Cyanidin-3-Glucoside (300–330 mg C3G, Module 37)**. C3G is a validated allosteric activator of **SIRT6** (accelerating catalytic deacetylation up to 55-fold), which directly mono-ADP-ribosylates **PARP-1 at Lys521** to drive non-homologous end joining (NHEJ) and base excision repair (BER) while silencing LINE-1 retrotransposons. AC-11 contributes zero marginal DNA repair alpha over C3G + intracellular Magnesium.
- **V5 Replacement:** Retired from active rotation ($25/mo + 2 caps/day saved). Rely on daily C3G + Magnesium L-Threonate.

### RET-07: Epitalon (Ala-Glu-Asp-Gly Pineal Tetrapeptide)
- **Historical Thesis:** Synthetic biomimetic of epithalamin hypothesized to interact with histone proteins and DNA promoter sequences to upregulate telomerase reverse transcriptase (TERT) and normalize circadian melatonin rhythmicity.
- **Empirical Cause for Termination:** Lowest Bayesian probability in the protocol (40%). Near-total absence of independent Western structural biology replication demonstrating sequence-specific binding to the *hTERT* promoter or histone displacement at physiological nanomolar concentrations.
- **Biophysical Mechanism of Failure & Redundancy:** Completely redundant with high-conviction protocol interventions: **Low-Dose Lithium (Module 25)** stimulates *hTERT* transcription via GSK-3$\beta$ inhibition and nuclear $\beta$-catenin stabilization; **2.0 ATA HBOT (Module 29)** and **TM5614 (Module 41)** robustly elongate leukocyte telomeres; and pineal circadian melatonin amplitude is protected by morning solar entrainment and nocturnal **taVNS + Glycine (Module 31)**.
- **V5 Replacement:** Retired from active rotation ($100–$140/yr + daily subcutaneous injection friction saved).

### RET-08: High-Dose Synthetic Oral Spermidine Trihydrochloride Capsules
- **Historical Thesis:** Ingesting 15–20 mg/day of synthetic spermidine trihydrochloride to drive eIF5A hypusination and TFEB-mediated lysosomal autophagy.
- **Empirical Cause for Termination:** High cost ($30+/mo) and physiological first-pass barriers. Human pharmacokinetic tracing demonstrates that exogenous oral spermidine undergoes rapid deamination by intestinal diamine oxidase (DAO) in the upper GI enterocyte brush border or enzymatic conversion into spermine, preventing significant expansion of systemic lymphocyte polyamine pools.
- **Biophysical Mechanism of Failure & V5 Replacement:** Transitioned entirely to the **Endogenous Colonic Bioreactor (Module 07 & 37)**: daily **Acarbose (Module 01) + retrograded RS3 resistant starch + Arginine/Ornithine + *Bifidobacterium animalis* subsp. *lactis* LKM512**. This drives continuous, high-volume polyamine generation in the cecum/colon, completely bypassing upper-GI DAO and absorbing directly into mesenteric portal blood at zero marginal capsule burden.

---

# SECTION XI: COMPREHENSIVE PHARMACOLOGICAL SAFETY & COLLISION MATRIX

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
