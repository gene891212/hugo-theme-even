import re

with open("/home/gene/blog/themes/even/assets/sass/_partial/_waline.scss") as f:
    content = f.read()

string = re.sub(r"var\(--(.*)\)", lambda x: f"${x.group(1)}", content)

with open("./waline_o.scss", "w") as f:
    f.write(string)
