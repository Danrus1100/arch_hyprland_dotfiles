#!/bin/bash

# Получаем список файлов в текущем каталоге
files=$(ls ~/wallpapers)

# Отображаем список файлов в Rofi и получаем выбранный файл
selected_file=$(echo "$files" | wofi --dmenu -w 3: -p "Select Wallpaper:")


# сделай условие что если как аргумент указан -t, то выбираем тему

if [ "$1" = "-t" ]; then
    theme="dark
light"
    theme=$(echo "$theme" | wofi --dmenu -p "Select Theme:")
fi


# Если файл был выбран, открываем его в nano
if [ -n "$selected_file" ]; then
    if [ "$theme" = "light" ]; then
        wal -i ~/wallpapers/"$selected_file" -l
    else
        wal -i ~/wallpapers/"$selected_file"
    fi
    #swww img ~/wallpapers/"$selected_file" --transition-fps=144 --transition-type=outer --transition-duration=1.5 --transition-pos top-right    
    swww img ~/wallpapers/"$selected_file" --transition-fps=144 --transition-type=center --transition-duration=1.5 --transition-pos "$(hyprctl cursorpos)" --invert-y    
    cp ~/.cache/wal/colors-waybar.css ~/.config/waybar/2/
    cp ~/.cache/wal/colors-waybar.css ~/.config/waybar/3/
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/stat_menu
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/wallpaper_selector
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/bar
    cp ~/.cache/wal/colors.json ~/bin/
    python ~/bin/walcord.py
    cp ~/bin/f_colors-modnight.css ~/.config/vesktop/themes
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/bg_clocks
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/lang_switch_notify
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/desktop_numbers
    pkill -SIGUSR2 waybar
    pywalfox update
else
   notify-send "Wallpaper dont selected!"
fi

