#!/bin/bash

# Получаем процент заряда батареи без символа %
battery_percentage=$(upower -i $(upower -e | grep battery) | grep -E "percentage" | awk '{print $2}' | tr -d '%')

# Определяем текст в зависимости от уровня заряда
if [ "$battery_percentage" -ge 0 ] && [ "$battery_percentage" -lt 10 ]; then
    echo "󰁺"
elif [ "$battery_percentage" -ge 10 ] && [ "$battery_percentage" -lt 20 ]; then
    echo "󰁻"
elif [ "$battery_percentage" -ge 20 ] && [ "$battery_percentage" -lt 30 ]; then
    echo "󰁼"
elif [ "$battery_percentage" -ge 30 ] && [ "$battery_percentage" -le 40 ]; then
    echo "󰁽"
elif [ "$battery_percentage" -ge 40 ] && [ "$battery_percentage" -le 50 ]; then
    echo "󰁾"
elif [ "$battery_percentage" -ge 50 ] && [ "$battery_percentage" -le 60 ]; then
    echo "󰁿"
elif [ "$battery_percentage" -ge 60 ] && [ "$battery_percentage" -le 70 ]; then
    echo "󰂀"
elif [ "$battery_percentage" -ge 70 ] && [ "$battery_percentage" -le 80 ]; then
    echo "󰂁"
elif [ "$battery_percentage" -ge 80 ] && [ "$battery_percentage" -le 90 ]; then
    echo "󰂂"
elif [ "$battery_percentage" -ge 90 ] && [ "$battery_percentage" -le 100 ]; then
    echo "󰂄"
else
    echo "Некорректное значение заряда батареи"
fi

