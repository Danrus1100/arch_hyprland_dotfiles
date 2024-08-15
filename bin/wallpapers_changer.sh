#!/bin/bash

# Получаем список файлов в текущем каталоге
files=$(ls ~/wallpapers)

# Отображаем список файлов в Rofi и получаем выбранный файл
selected_file=$(echo "$files" | wofi --dmenu -p "Select Wallpaper:")

# Если файл был выбран, открываем его в nano
if [ -n "$selected_file" ]; then
    swww img ~/wallpapers/"$selected_file" --transition-fps=144 --transition-type=outer --transition-duration=1 --transition-pos top-right    
    wal -i ~/wallpapers/"$selected_file"
    cp ~/.cache/wal/colors-waybar.css ~/.config/waybar/2/
    cp ~/.cache/wal/colors-waybar.css ~/.config/eww/stat_menu
    pkill -SIGUSR2 waybar
    sh ~/bin/themecord.sh
    pywalfox update
else
   notify-send "Wallpaper dont selected!"
fi

