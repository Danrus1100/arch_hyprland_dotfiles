import json
import os

os.chdir('/home/danrus/bin')
colors_dir = "./colors.json"
theme_dir = "./colors-modnight.css"
final_dir = "./f_colors-modnight.css"

with open(colors_dir, "r") as read_file:
    colors = json.load(read_file)

with open(theme_dir, "r") as read_file:
    text = read_file.read()

wal_colors = {
    "KEY_BACKGROUND": colors["special"]["background"],
    "KEY_BORDER": colors["colors"]["color2"],
    "KEY_TEXT": colors["colors"]["color15"],
    "KEY_ACCENT": colors["colors"]["color13"]
    }

for key in wal_colors:
    text = text.replace(key, wal_colors[key])

read_file.close()

with open(final_dir, "w") as write_file:
    write_file.write(text)

write_file.close()
