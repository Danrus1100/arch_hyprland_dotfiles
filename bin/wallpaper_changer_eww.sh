#!/bin/bash

eww close wallpapers -c ~/.config/eww/wallpaper_selector
swww img "$1" --transition-fps=144 --transition-type=outer --transition-duration=1.5 --transition-pos top-right
wal -i "$1"
cp ~/.cache/wal/colors-waybar.css ~/.config/waybar/2/
cp ~/.cache/wal/colors-waybar.css ~/.config/waybar/3/
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/stat_menu
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/bar
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/wallpaper_selector
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/power_menu
cp ~/.cache/wal/colors.json ~/bin/
python ~/bin/walcord.py 
cp ~/bin/f_colors-modnight.css ~/.config/vesktop/themes
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/bg_clocks
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/lang_switch_notify
cp ~/.cache/wal/colors-waybar.css ~/.config/eww/desktop_numbers
pkill -SIGUSR2 waybar
pywalfox update 
walogram -B
sh ~/pywal-obsidianmd/pywal-obsidianmd.sh "/home/danrus/Документы/obsidian/Brain"
#sleep 10
#eww close menu -c ~/.config/eww/wallpaper_selector 
