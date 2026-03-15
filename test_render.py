import re
with open("GeoCharterly_P01.html", "r") as f:
    text = f.read()

print(re.search(r'<div class="logo" onclick="goStep\(-1\)"', text) is not None)
