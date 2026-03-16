import re

with open("Charterly_RICS_Claude P02 (7).html", "r") as f:
    content = f.read()

# Add missing `selSector` function that was lost during git gymnastics
new_funcs = """
function selSector(sec) {
  if (S.sector === sec) return;
  S.sector = sec;
  S.pathway = null;
  S.subDesig = null;
  S.desig = null;
  S.sel.spec = null;
  S.sel.core = [];
  S.sel.opt = [];
  S.sel.tech = null;
  saveState();
  render();
}
"""

# Find where to put it. Just before `function selPathway(key)`
match = re.search(r'function selPathway\(key\)', content)
if match:
    idx = match.start()
    content = content[:idx] + new_funcs + content[idx:]
    with open("Charterly_RICS_Claude P02 (7).html", "w") as f:
        f.write(content)
        print("Injected selSector!")
else:
    print("Could not find selPathway!")
