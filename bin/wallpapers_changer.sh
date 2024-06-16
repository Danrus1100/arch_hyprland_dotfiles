#!/bin/bash

# Получаем список файлов в текущем каталоге
files=$(ls ~/wallpapers)

# Отображаем список файлов в Rofi и получаем выбранный файл
selected_file=$(echo "$files" | wofi --dmenu -p "Select Wallpaper:")

# Если файл был выбран, открываем его в nano
if [ -n "$selected_file" ]; then
    swww img ~/wallpapers/"$selected_file" --transition-fps=144 --transition-type=outer --transition-duration=1
else
   notify-send "Wallpaper dont selected!"
fi

