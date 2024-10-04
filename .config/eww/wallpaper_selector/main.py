import hashlib
import os
import subprocess
from PIL import Image

XDG_CONFIG_HOME = os.getenv('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))
USER_NAME = os.popen("whoami").read()[:-1]
WALLPAPERS_DIRECTORY = f"/home/{USER_NAME}/wallpapers/"
CACHE_DIRECTORY = f"/home/{USER_NAME}/.cache/wallpaper_selector/"
TEMPLATE_FILE = os.path.join(XDG_CONFIG_HOME, 'eww/wallpaper_selector/eww.yuck_')
MENU_ROWS = 3
MENU_WIDTH = 25 - MENU_ROWS * 2 if MENU_ROWS > 2 else 25

def get_wallpapers(dir: str):
    with os.scandir(dir) as entries:
        return [entry.name for entry in entries if entry.is_file()]

def create_previews(wallpapers: list): 
    os.makedirs(CACHE_DIRECTORY, exist_ok=True)
    for wallpaper in wallpapers:
        if not os.path.exists(os.path.join(CACHE_DIRECTORY, os.path.splitext(wallpaper)[0] + ".png")):
            print("creating " + os.path.join(CACHE_DIRECTORY, wallpaper))
            img = Image.open(os.path.join(WALLPAPERS_DIRECTORY, wallpaper))
            size = min(img.size)
            width, height = img.size
            if width != height:
                size = min(img.size)
                left = (width - size) // 2
                top = (height - size) // 2
                img = img.crop((left, top, left + size, top + size))
            img = img.resize((480, 480))
            img.save(CACHE_DIRECTORY + os.path.splitext(wallpaper)[0] + '.png', format='PNG')
            img.close()
        else:
            print(f"Skipping {wallpaper} as it already exists in {CACHE_DIRECTORY}")

def create_string(wal: list, wal_names, rows: int):
    string = ""
    row = 1
    line_s = ""
    line_s_begin = "(box :orientation 'h' :spacing 5 "

    for wallpaper in range(len(wal)):
        if row == 1:
            line_s += line_s_begin

        if wal_names[wallpaper] == "":
            code_str = ""
        else:
            code_str = f"(button :onclick 'python ~/bin/wallpaper_changer_eww.py {WALLPAPERS_DIRECTORY}{wal[wallpaper]}'(box :orientation 'h' :class 'btn' (image :path '{CACHE_DIRECTORY}{wal_names[wallpaper]}.png' :image-width {int(400 / MENU_ROWS) if MENU_ROWS > 1 else 200}) '{wal_names[wallpaper]}'))"

        #line_s += f"(box :orientation 'h' :class 'btn' (image :path '{CACHE_DIRECTORY}{wal_names[wallpaper]}.png' :image-width {int(400 / MENU_ROWS) if MENU_ROWS > 1 else 200}) (button :onclick 'python ~/bin/wallpaper_changer_eww.py {WALLPAPERS_DIRECTORY}{wal[wallpaper]}' '{wal_names[wallpaper]}')) "
        line_s += code_str

        if row == rows:
            line_s += ")"
            row = 0
            string = string + line_s
            line_s = ""
        row += 1

    return string

def cache_has_all_wallpapers():
    wallpapers = os.listdir(WALLPAPERS_DIRECTORY)
    cached_wallpapers = os.listdir(CACHE_DIRECTORY)
    for wallpaper in wallpapers:
        if not os.path.exists(os.path.join(CACHE_DIRECTORY, os.path.splitext(wallpaper)[0] + '.png')):
            return True

    return False

def clear_cache():
    print("Checking for missing wallpapers...")
    wallpapers = set(os.path.splitext(w)[0] for w in os.listdir(WALLPAPERS_DIRECTORY))
    cached_wallpapers = set(os.path.splitext(w)[0] for w in os.listdir(CACHE_DIRECTORY))
    for wallpaper in cached_wallpapers - wallpapers:
        print(f"Removing {wallpaper}.png from {CACHE_DIRECTORY} as it no longer exists in {WALLPAPERS_DIRECTORY}")
        os.remove(os.path.join(CACHE_DIRECTORY, wallpaper + '.png'))

def file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def open_menu():
    print("Running command to open menu...")
    result = subprocess.run("eww open wallpapers -c ~/.config/eww/wallpaper_selector --toggle", shell=True)
    print(f"Command executed with return code: {result.returncode}")
    if result.returncode != 0:
        print(f"Error occurred: {result.stderr}")


def main():
    print("Starting wallpaper selector")

    if cache_has_all_wallpapers():
        print("Creating cache...")
        create_previews(os.listdir(WALLPAPERS_DIRECTORY))
    else:
        clear_cache()
        print("Cache already exists. Skipping creation...")

    wallpapers = get_wallpapers(WALLPAPERS_DIRECTORY)
    print("Found " + str(len(wallpapers)) + " wallpapers")
    wallpapers_names = [os.path.splitext(w)[0] for w in wallpapers]
    if len(wallpapers) % MENU_ROWS != 0:
        wallpapers += [''] * (MENU_ROWS - len(wallpapers) % MENU_ROWS)
        wallpapers_names += [''] * (MENU_ROWS - len(wallpapers_names) % MENU_ROWS)
    print("Creating eww.yuck...")

    file_content = open(TEMPLATE_FILE, "r").read()
    file_content = file_content.replace("KEY_BTNS", create_string(wallpapers, wallpapers_names, MENU_ROWS))
    file_content = file_content.replace("KEY_WIDTH", str(MENU_WIDTH * MENU_ROWS))

    temp_file_path = f"/home/{USER_NAME}/.config/eww/wallpaper_selector/eww_temp.yuck"
    with open(temp_file_path, "w") as temp_file:
        temp_file.write(file_content)

    if not os.path.exists(f"/home/{USER_NAME}/.config/eww/wallpaper_selector/eww.yuck") or file_hash(temp_file_path) != file_hash(f"/home/{USER_NAME}/.config/eww/wallpaper_selector/eww.yuck"):
        os.replace(temp_file_path, f"/home/{USER_NAME}/.config/eww/wallpaper_selector/eww.yuck")
        print("eww.yuck updated.")
    else:
        os.remove(temp_file_path)
        print("No changes detected, eww.yuck not updated.")

    
    open_menu()

if __name__ == "__main__":
    main()