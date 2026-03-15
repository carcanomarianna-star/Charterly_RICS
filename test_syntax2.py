import re

with open("test.js", "r") as f:
    js = f.read()

# Count the braces
open_braces = js.count("{")
close_braces = js.count("}")

print(f"Open: {open_braces}")
print(f"Close: {close_braces}")
