import re

with open("GeoCharterly_P01.html", "r") as f:
    content = f.read()

# Remove the leftover bits of the pathway guide chart logic
content = re.sub(r'                        \}\n                    \},\n                    plugins: \{.*?\n                    \}\n                \}\n            \}\);\n', '', content, flags=re.DOTALL)

with open("GeoCharterly_P01.html", "w") as f:
    f.write(content)
