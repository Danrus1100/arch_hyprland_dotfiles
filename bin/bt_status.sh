#!/bin/bash

# Проверка состояния Bluetooth
bluetooth_status=$(rfkill list bluetooth | grep -i "Soft blocked: no")

if [ -n "$bluetooth_status" ]; then
    echo "󰂯"
else
    echo "󰂲"
fi

