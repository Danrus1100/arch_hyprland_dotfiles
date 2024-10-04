#!/bin/bash


# Проверяем наличие активного интерфейса WireGuard с IP-адресом
if wg show | grep -q "peer"; then
    wg-quick down /home/danrus/vpn.conf  # Останавливаем VPN
    echo "VPN выключен"
else
    wg-quick up /home/danrus/vpn.conf  # Запускаем VPN
    echo "VPN включён"
fi

