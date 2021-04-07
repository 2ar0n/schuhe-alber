from shutil import copyfile
import yaml
import re

lang_files = ["de.yaml", "it.yaml", "en.yaml"]

base_file = "base.html"

for lang_file in lang_files:

    html = open(base_file, "r").read()
    lang_yaml = yaml.safe_load(open(lang_file, "r"))

    def from_yaml(dct):
        def lookup(match):
            placeholder = match.group(1)

            a = dct
            for key in placeholder.strip().split("."):
                a = a[key]
            return a
        return lookup

    text = re.sub("{{(.*?)}}", from_yaml(lang_yaml), html)

    target_file = "_site/" + lang_file.split(".")[0] + ".html"
    open(target_file, "w").write(text)

    print(f"Generated page from {lang_file}")
