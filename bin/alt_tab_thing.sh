$json_hypr=hyprctl clients -j

hyprctl clients -j | jq '.[] | .initialClass' | sed 's/["]//g' | awk '{print(NR " " $0)}' | wofi --dmenu | cut -f1 -d" " | jq '.[$0].workspace.id' $json_hypr
