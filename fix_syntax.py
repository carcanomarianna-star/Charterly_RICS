import re

with open("GeoCharterly_P01.html", "r") as f:
    content = f.read()

# Ah! It looks like there's another missing bracket in calcProgress. Let's fix calcProgress properly.
# The original calcProgress logic had more code before my regex removed it accidentally.
# Let's restore the full original calcProgress minus CICES stuff.
calc_progress_original = """
function calcProgress() {
  const comps = buildAllComps();
  // RPQ route: progress is CPD-only (no statements or case study)
  if (isRPQRoute()) {
    const cpdEntries = S.cpd || [];
    const cvEntries  = S.cv  || [];
    const cpdOk = cpdEntries.length > 0;
    const cvOk  = cvEntries.length  > 0;
    return Math.round(((cpdOk ? 1 : 0) + (cvOk ? 1 : 0)) / 2 * 100);
  }

  let total=0, done=0;
  // Statements
  comps.forEach(comp => {
    for (let l=1; l<=comp.req; l++) {
      total += getWordTarget(comp, l);
      done  += Math.min(cw(S.statements[`${comp.id}_L${l}`]), getWordTarget(comp, l));
    }
  });
  // Case Study
  total += 3000;
  done  += Math.min(cw(S.caseStudy), 3000);
  return Math.min(Math.round((done/total)*100), 100);
}
"""
content = re.sub(r'function calcProgress\(\) \{.*\}  return 100; // Placeholder for non-RPQ progress\n\}', calc_progress_original, content, flags=re.DOTALL)

with open("GeoCharterly_P01.html", "w") as f:
    f.write(content)
