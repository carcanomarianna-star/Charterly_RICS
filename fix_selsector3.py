with open("Charterly_RICS_Claude P02 (7).html", "r") as f:
    content = f.read()

# wait, I did inject selSector in the first commit (f9d76a2) right?
# Let's check where it got injected!
import re
match = re.search(r'function selSector', content)
if match:
    idx = match.start()
    print("Found selSector at", idx)
    print(content[max(0, idx-500):idx+500])
else:
    print("No selSector found!!!")
