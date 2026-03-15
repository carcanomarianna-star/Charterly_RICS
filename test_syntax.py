import re
with open("GeoCharterly_P01.html", "r") as f:
    content = f.read()

match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if match:
    with open("test.js", "w") as f:
        f.write(match.group(1))
