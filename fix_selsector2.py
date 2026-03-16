import re

with open("Charterly_RICS_Claude P02 (7).html", "r") as f:
    content = f.read()

# Ah, `selPathway` might have been a `const` or inside an object, or it wasn't there at all in the original file?!
# Wait, let's look at `function r1` where `selPathway` is CALLED.

match = re.search(r'function r1\(C\)', content)
if match:
    idx = match.start()

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

function selPathway(key) {
  if (S.pathway === key) return;
  S.pathway = key;
  S.subDesig = null;
  S.desig = null;
  S.sel.spec = null;
  S.sel.core = [];
  S.sel.opt = [];
  S.sel.tech = null;
  saveState();
  render();
}

function selSubDesig(d) {
  S.subDesig = d;
  S.desig = d; // legacy alias
  // auto-select matching specialism
  const desigs = getDesigs();
  if (desigs) {
    const spec = desigs.find(x => x.id === d);
    if (spec) S.sel.spec = spec.specId;
  }
  saveState();
  render();
}

"""
    content = content[:idx] + new_funcs + content[idx:]
    with open("Charterly_RICS_Claude P02 (7).html", "w") as f:
        f.write(content)
        print("Injected functions before r1(C)!")
else:
    print("Could not find r1(C)!")
