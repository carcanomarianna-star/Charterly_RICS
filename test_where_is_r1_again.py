import re
with open("Charterly_RICS_Claude P02 (7).html", "r") as f:
    content = f.read()

match = re.search(r'function r1\(C\)', content)
if match:
    idx = match.start()
    print(content[max(0, idx-500):idx+500])
