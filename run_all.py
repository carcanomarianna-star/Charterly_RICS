import re

with open("GeoCharterly_P01.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove CSS
html = re.sub(r'    --cices:        #2E4D3B;\n    --cices-bright: #4a7a61;\n    --cices-bg:     #e4ede8;\n    --cices-border: #84B399;\n    --cices-grd:    linear-gradient\(135deg,#2E4D3B,#84B399,#2E4D3B\);\n', '', html)
html = re.sub(r'  body\.cices-mode \{\n.*?\}\n', '', html, flags=re.DOTALL)
html = re.sub(r'  /\* CICES card \*/\n  \.cices-card:hover,\.cices-card\.selected\{border-color:var\(--cices\);background:var\(--cices-bg\)\}\n  \.cices-card:hover\{box-shadow:0 6px 24px rgba\(46,77,59,\.25\);transform:translateY\(-2px\)\}\n  \.cices-card::before\{background:var\(--cices-grd\)\}\n  \.cices-card:hover::before,\.cices-card\.selected::before\{opacity:1\}\n', '', html)
html = re.sub(r'  \.badge-cices\{background:var\(--cices-bg\);color:var\(--cices-bright\);border:1px solid var\(--cices-border\)\}\n', '', html)
html = re.sub(r'  \.badge-green\{background:var\(--cices-bg\);color:var\(--cices\);border:1px solid var\(--cices-border\)\}\n', '  .badge-green{background:#e8f5e9;color:#2e7d52;border:1px solid #a8d5b5}\n', html)
html = re.sub(r'  \.btn-export\{background:var\(--cices-bg\);color:var\(--cices\);border:1px solid var\(--cices-border\);font-size:14px;padding:12px 28px\}\n  \.btn-export:hover\{background:var\(--cices-border\);color:#fff\}\n', '', html)
html = re.sub(r'  \.comp-row\.locked     \{border-color:var\(--cices-border\);background:var\(--cices-bg\);cursor:default;opacity:1\}\n', '  .comp-row.locked     {border-color:var(--rics-border);background:var(--rics-bg);cursor:default;opacity:1}\n', html)
html = re.sub(r'  \.chk-lock-g\{width:17px;height:17px;border-radius:4px;flex-shrink:0;border:2px solid var\(--cices-bright\);background:var\(--cices-bright\);display:flex;align-items:center;justify-content:center\}\n', '', html)
html = re.sub(r'  /\* CICES Competency tickbox styles \*/.*?\.cices-specialism-card \.sp-name \{ font-size:14px; font-weight:600; color:var\(--text\); margin-top:2px; \}\n', '', html, flags=re.DOTALL)
html = re.sub(r'  \.ai-modal\.cices \{ border-color: #84B399; border-top-color: #2E4D3B; \}\n  \.ai-modal\.cices \.ai-modal-badge \{ background:#EAF2ED; border-color:#84B399; color:#2E4D3B; \}\n  \.ai-modal\.cices \.ai-modal-title \{ color:#2E4D3B; \}\n  \.ai-modal\.cices \.ai-modal-body em \{ color:#2E4D3B; \}\n  \.ai-modal\.cices \.ai-modal-understand \{ background:#2E4D3B; \}\n', '', html)
html = re.sub(r'  /\* CICES mode — override all stab active states with CICES palette \*/\n  body\.cices-mode \.stab\.active        \{ background: var\(--cices-bg\); color: var\(--cices\); border-color: var\(--cices-border\); \}\n  body\.cices-mode \.stab\.stab-cpd\.active \{ background: var\(--cices-bg\); color: var\(--cices\); border-color: var\(--cices-border\); \}\n  body\.cices-mode \.stab\.stab-cs\.active  \{ background: var\(--cices-bg\); color: var\(--cices\); border-color: var\(--cices-border\); \}\n  body\.cices-mode \.stab\.stab-cv\.active  \{ background: var\(--cices-bg\); color: var\(--cices\); border-color: var\(--cices-border\); \}\n  body\.cices-mode \.stab:hover           \{ background: var\(--cices-bg\); color: var\(--cices\); \}\n  body\.cices-mode \.step-item\[data-step="2"\] \{ display: none; \}\n', '', html)
html = re.sub(r'  /\* ── CICES 3-column layout \(cross-ref \| main \| guidance\) ── \*/\n  \.cices-3col \{.*?\n  \.cices-comp-nav    \{ display: none; \}\n  \}\n', '', html, flags=re.DOTALL)

# 2. Remove Pathway guide & comparison elements
html = re.sub(r'  /\* ── Pathway Guidance card ──────────────────────────────────────── \*/\n  \.pathway-card\{flex:1;min-width:200px;max-width:300px;border:2px solid #9FBBCF;background:linear-gradient\(160deg,#EEF5FA 0%,#dceaf3 100%\);border-radius:12px;padding:22px 20px;cursor:pointer;transition:all \.18s;position:relative;overflow:hidden;text-align:center;display:flex;flex-direction:column;justify-content:space-between\}\n  \.pathway-card:hover\{border-color:#7aa8c4;box-shadow:0 6px 24px rgba\(159,187,207,\.4\);transform:translateY\(-2px\)\}\n  \.pathway-card \.choice-label\{font-size:20px;font-weight:700;color:#3a6a8a;margin-bottom:6px;letter-spacing:\.01em\}\n  \.pathway-card \.choice-desc\{font-size:12\.5px;color:#4a6070;margin-bottom:14px;line-height:1\.5\}\n  \.pathway-card \.pg-badge\{display:inline-block;font-family:\'DM Mono\',monospace;background:#9FBBCF;color:#1a3d52;border:1px solid #7fa8c0;border-radius:3px;font-size:10px;font-weight:500;padding:2px 8px;letter-spacing:\.05em\}\n', '', html)
html = re.sub(r'function rPathwayGuidance\(C\) \{.*?\}\n', '', html, flags=re.DOTALL)

# 3. Clean JS S object properties
html = html.replace("cicesSpecialism: null,   // \"GEES\"|\"GELS\"|\"GEUS\"|\"GES3\"\n", "")
html = html.replace("  cicesGrades: {},           // {\"GEN01_A\":\"E\", \"GECORE01_B\":\"K\", ...} — candidate self-assessed grade per activity\n", "")
html = re.sub(r',\s*cicesSpecialism:null', '', html)

# 4. Remove CICES competencies data
html = re.sub(r'// ══════════════════════════════════════════════ CICES COMPETENCY DATA ════════.*?// ─── CICES Step 1: Pathway/Specialism Selection ───────────────────────────────\n', '', html, flags=re.DOTALL)
html = re.sub(r'function toggleCicesGroup\(compId\) \{.*?// ─── CICES Step 2: Competency Tickbox ─────────────────────────────────────────\n', '', html, flags=re.DOTALL)
html = re.sub(r'function r2Cices\(C\) \{.*?\n\}\n\n', '', html, flags=re.DOTALL)
html = re.sub(r'function r4Cices\(C\) \{.*?\n\}\n\n', '', html, flags=re.DOTALL)
html = re.sub(r'function rCPD_CICES\(C\) \{.*?\n\}\n\n', '', html, flags=re.DOTALL)
html = re.sub(r'// ── CICES CPD Helpers ──────────────────────────────────────────────────────.*?// ── END CICES CPD', '', html, flags=re.DOTALL)
html = re.sub(r'function renderCPDForm_CICES\(container\) \{.*?\n\}\n\n', '', html, flags=re.DOTALL)
html = re.sub(r'function cpdSaveFormCICES\(\) \{.*?\n\}\n\n', '', html, flags=re.DOTALL)
html = re.sub(r'// CICES: competencies \+ CPD \+ experience report \+ CV.*?\}\n\n', '', html, flags=re.DOTALL)

# Clean up step 0 / Body selection logic
html = re.sub(r'function r0\(C\) \{.*?\}\nfunction selBody\(b\) \{.*?\}\nfunction confirmBodyAndContinue\(\) \{.*?\}\n', '', html, flags=re.DOTALL)

# Clean rendering logic
html = re.sub(r'function pgInit\(\) \{.*?\}\s*function loadScript\(src, cb\) \{', 'function loadScript(src, cb) {', html, flags=re.DOTALL)
html = re.sub(r'  function loadCss\(href\) \{.*?\n\}\n\nfunction render\(\) \{', 'function render() {', html, flags=re.DOTALL)
html = re.sub(r'\s*if \(S\.step === -2\) \{\s*rPathwayGuidance\(mainEl\);\s*\} else if \(S\.step === -1\) \{', '\n    if (S.step === -1) {', html, flags=re.DOTALL)
html = html.replace("[r0,r1,r2,r3][S.step](mainEl);", "[r0,r1,r2,r3][S.step](mainEl);")
html = html.replace("""      } else if (S.body === "CICES" && s === 2) {
        // CICES skips step 2 — "Competencies" in stepbar goes to step 3 competencies tab
        el.className = "step-item" + (S.step===3&&S.activeSection==='competencies' ? " active" : S.step>2 ? " done" : "");
        el.onclick = S.step >= 3 ? () => { S.activeSection='competencies'; goStep(3); } : null;
        el.title = "CICES Competency Log";""", "")
html = html.replace("if (S.body === \"CICES\") { r1Cices(C); return; }", "")
html = html.replace("if (S.body === \"CICES\") { r2Cices(C); return; }", "")
html = html.replace("if (S.body === \"CICES\") { r4Cices(C); return; }", "")
html = html.replace("if (S.body === \"CICES\") { cicesCpdUploadCSV(input); return; }", "")
html = html.replace("if (S.body === \"CICES\" && S.activeSection === \"competencies\") { r2Cices(C); return; }", "")
html = html.replace("if (S.body === \"CICES\" && S.activeSection === \"experiencereport\") { r4Cices(C); return; }", "")
html = html.replace("const _isCICES_r3 = S.body === \"CICES\";", "const _isCICES_r3 = false;")

# Remove the RICS/CICES tab blocks
html = re.sub(r'  if \(_isCICES_r3\) \{.*?  \} else \{\n    _r3TabsDiv = buildRicsStabBar', '  _r3TabsDiv = buildRicsStabBar', html, flags=re.DOTALL)
html = re.sub(r'  const _isCICES_r4 = S\.body === "CICES";\n  let tabsWrap;\n  if \(_isCICES_r4\) \{.*?  \} else \{\n    tabsWrap = buildRicsStabBar', '  let tabsWrap;\n  tabsWrap = buildRicsStabBar', html, flags=re.DOTALL)
html = html.replace("S.body==='RICS'", "true")


# Add RICS pathways data and new r1/r0 function
pathway_scaffold = """
function r0(C) {
  C.innerHTML=`<div class="page-centre"><div class="panel" style="text-align:center;padding:60px 40px;">
    <h1 class="page-title" style="font-size:32px;margin-bottom:16px">Welcome to GeoCharteRly</h1>
    <p class="sub" style="font-size:16px;max-width:600px;margin:0 auto 32px">Prepare your RICS submission with confidence.</p>
    <button class="btn btn-primary" style="font-size:16px;padding:14px 32px" onclick="goStep(-1)">Start Eligibility Assessment →</button>
  </div></div>`;
}

const RICS_PATHWAYS = [
  { id: "geomatics", name: "Geomatics", status: "active" },
  { id: "building_surveying", name: "Building Surveying", status: "coming_soon" },
  { id: "commercial_real_estate", name: "Commercial Real Estate", status: "coming_soon" },
  { id: "construction", name: "Construction", status: "coming_soon" },
  { id: "corporate_real_estate", name: "Corporate Real Estate", status: "coming_soon" },
  { id: "environmental_surveying", name: "Environmental Surveying", status: "coming_soon" },
  { id: "facilities_management", name: "Facilities Management", status: "coming_soon" },
  { id: "infrastructure", name: "Infrastructure", status: "coming_soon" },
  { id: "land_and_resources", name: "Land and Resources", status: "coming_soon" },
  { id: "management_consultancy", name: "Management Consultancy", status: "coming_soon" },
  { id: "minerals_and_waste", name: "Minerals and Waste Management", status: "coming_soon" },
  { id: "personal_property", name: "Personal Property/Arts and Antiques", status: "coming_soon" },
  { id: "planning_and_development", name: "Planning and Development", status: "coming_soon" },
  { id: "project_management", name: "Project Management", status: "coming_soon" },
  { id: "property_finance_and_investment", name: "Property Finance and Investment", status: "coming_soon" },
  { id: "quantity_surveying", name: "Quantity Surveying", status: "coming_soon" },
  { id: "residential", name: "Residential", status: "coming_soon" },
  { id: "rural", name: "Rural", status: "coming_soon" },
  { id: "taxation_allowances", name: "Taxation Allowances", status: "coming_soon" },
  { id: "valuation", name: "Valuation", status: "coming_soon" },
  { id: "valuation_of_businesses", name: "Valuation of Businesses and Intangible Assets", status: "coming_soon" },
  { id: "research", name: "Research", status: "coming_soon" },
  { id: "academic", name: "Academic", status: "coming_soon" }
];

function r1(C) {
  let pathwayOptionsHTML = '';
  RICS_PATHWAYS.forEach(pathway => {
    const isSelected = S.pathway === pathway.id;
    const isComingSoon = pathway.status === "coming_soon";
    const disabledAttr = isComingSoon ? 'disabled style="opacity:0.5;cursor:not-allowed;"' : '';
    const badgeHTML = isComingSoon ? '<span class="badge badge-muted">Coming Soon</span>' : '';

    pathwayOptionsHTML += `
      <div class="choice-card ${isSelected?'selected':''}" onclick="${isComingSoon ? '' : `selPathway('${pathway.id}')`}" ${disabledAttr}>
        <div class="choice-label" style="font-size:16px;color:var(--accent)">${pathway.name}</div>
        ${badgeHTML}
      </div>
    `;
  });

  C.innerHTML=`<div class="page-centre"><div class="panel">
    <h1 class="page-title">Select RICS Sector Pathway</h1>
    <p class="sub">Choose your RICS sector pathway to proceed.</p>
    <div class="choice-grid">
      ${pathwayOptionsHTML}
    </div>
    <div class="btn-row">
      <button class="btn btn-ghost" onclick="goStep(0)">← Back</button>
      <button class="btn btn-primary" ${!S.pathway?'disabled':''} onclick="goStep(2)">Continue →</button>
    </div>
  </div></div>`;
}

function selPathway(p) {
  S.pathway=p;
  // Default to 'eng' designation for Geomatics so specialism works
  if (p === 'geomatics') {
    S.desig = 'eng';
    S.sel.spec = DESIG_SPEC[S.desig]||null;
    if (S.sel.spec) {
      const sb = boOf(S.sel.spec, CORE_LIST);
      S.sel.core = S.sel.core.filter(id => boOf(id,CORE_LIST)!==sb);
    }
  }
  saveState();
  render();
}
"""

html = re.sub(r'function r1\(C\) \{.*?function selDesig\(d\) \{.*?\}\n', pathway_scaffold + '\n', html, flags=re.DOTALL)

# Setup initial state S
html = html.replace("let S = {\n  step: -2,", "let S = {\n  step: 0,\n  pathway: null,")
html = html.replace("if (S.body) document.body.className = (S.body===\"RICS\"?\"rics-mode\":S.body===\"CICES\"?\"cices-mode\":\"\") + (isRPQRoute()?\" rpq-mode\":\"\");", "document.body.className = (isRPQRoute()?\" rpq-mode\":\"\");")
html = html.replace("[r0,r1,r2,r3][S.step](mainEl);", "[r0,r1,r2,r3][S.step](mainEl);")
html = html.replace("goStep(-2)", "goStep(0)")

with open("GeoCharterly_P01.html", "w", encoding="utf-8") as f:
    f.write(html)

print("CICES removal & scaffold implemented.")
