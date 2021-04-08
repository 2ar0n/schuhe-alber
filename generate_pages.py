from shutil import copyfile
import yaml
import re
import argparse

parser = argparse.ArgumentParser(description="Generate website pages.")
parser.add_argument("--preview", action="store_true", help="Generate only german page")

args = parser.parse_args()

if args.preview:
    lang_files = ["de.yaml"]
else:
    lang_files = ["de.yaml", "it.yaml", "en.yaml"]

base_file = "base.html"
target_dir = "_site"

html = open(base_file, "r").read()

for lang_file in lang_files:
    lang_yaml = yaml.safe_load(open(lang_file, "r"))

    def from_yaml(yaml):
        def placeholder_content_from_yaml(match):
            placeholder = match.group(1)

            try:
                entry = yaml
                for key in placeholder.strip().split("."):
                    entry = entry[key]
                return entry
            except KeyError:
                print(f"Err: failed to find entry for \"{placeholder.strip()}\" in {lang_file}.")
        return placeholder_content_from_yaml

    text = re.sub("{{(.*?)}}", from_yaml(lang_yaml), html)

    target_file = target_dir + "/" + lang_file.split(".")[0] + ".html"
    open(target_file, "w").write(text)

    print(f"Generated {target_file} from {lang_file}\n")

copyfile("index.html", target_dir + "/index.html")
copyfile("styles.css", target_dir + "/styles.css")