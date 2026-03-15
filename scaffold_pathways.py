import re

with open("GeoCharterly_P01.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add RICS pathways data and new r1 function
pathway_scaffold = """
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

# Replace old r1 and selDesig
html = re.sub(r'function r1\(C\) \{.*?function selDesig\(d\) \{.*?\}\n', pathway_scaffold + '\n', html, flags=re.DOTALL)

with open("GeoCharterly_P01.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Scaffold implemented.")
