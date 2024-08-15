#!/bin/bash

# Проверка текущего состояния Bluetooth
bluetooth_status=$(rfkill list bluetooth | grep -i "Soft blocked: no")

if [ -n "$bluetooth_status" ]; then
    # Если Bluetooth включен, выключаем его
    rfkill block bluetooth
    echo "Bluetooth выключен"
else
    # Если Bluetooth выключен, включаем его
    rfkill unblock bluetooth
    echo "Bluetooth включен"
fi

