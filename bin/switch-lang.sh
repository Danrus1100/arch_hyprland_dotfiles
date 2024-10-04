hyprctl \
  --batch "$(
    hyprctl devices -j |
      jq -r '.keyboards[] | .name' |
      while IFS= read -r keyboard; do
        printf '%s %s %s;' 'switchxkblayout' "${keyboard}" 'next'
      done
  )"

eww open lang -c ~/.config/eww/lang_switch_notify 
sleep 0.5
eww close lang -c ~/.config/eww/lang_switch_notify 
