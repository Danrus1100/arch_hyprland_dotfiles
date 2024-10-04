import argparse
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

class Item:
    def __init__(self, file: str, prew_path: str) -> None:
        self.__file = file
        self.__name = file.split()[0]
        self.__prew_path = prew_path
        self.__eww_string = f"(box :orientation 'h' :class 'btn' (image :path '{CACHE_DIRECTORY}{name}.png' :image-width {int(400 / MENU_ROWS) if MENU_ROWS > 1 else 200}) (button :onclick 'python ~/bin/wallpaper_changer_eww.py {WALLPAPERS_DIRECTORY}{wal[wallpaper]}' '{wal_names[wallpaper]}')) "

    # Getter methods
    def get_name(self) -> str:
        return self.__name

    def get_file(self) -> str:
        return self.__file

    def get_prew_path(self) -> str:
        return self.__prew_path

    # Setter methods
    def set_name(self, name: str) -> None:
        self.__name = name

    def set_file(self, file: str) -> None:
        self.__file = file

    def set_prew_path(self, prew_path: str) -> None:
        self.__prew_path = prew_path

    # String representation
    def __str__(self) -> str:
        return f"Item(name={self.__name}, file={self.__file}, prew_path={self.__prew_path})"

def default_action():
    print("No arguments have been given. Use -h or --help for help")
    exit()
    
def main() -> None:
    parser = argparse.ArgumentParser(description="Wallpaper changer for EWW + SWWW")
    parser.add_argument("-m", '--menu', type=int , help="Open the menu with wallpaper selection. Enter the number of columns")
    parser.add_argument("-p", '--previews', action='store_true', help="Checks and creates previews for menu if necessary")
    parser.add_argument("-fp", '--force-previews', action='store_true', help="Creates previews without checking")
    
    args = parser.parse_args()


    if not (args.previews or args.force_previews or args.menu):
        default_action()

    if args.previews:
        print(123)
    if


if __name__ == "__main__":
    main()