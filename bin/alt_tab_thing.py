import os
import json
import subprocess

hyprctl_clients = json.load(os.popen("hyprctl clients -j"))
clients = list()
i = 0
for client in hyprctl_clients:
    clients.append({
        "title" :client["initialTitle"],
        "number": i+1, 
        "workspace": client["workspace"]["id"],
        "name": client["title"]})
    i += 1

menu_text = ""
add_text = "\n"
kitty_title = ""
i = 0

for client in clients:
    kitty_title = ""
    if len(clients) == clients[i]["number"]:
        add_text = ""
    if client["title"] == "kitty":
        kitty_title = ": "+client["name"]
    menu_text += f"{client['number']} {client['title']} {kitty_title} {add_text}"
    i+=1

answer = subprocess.check_output(f"echo '{menu_text}' | wofi --dmenu --sort-order", shell=True, capture_output=False,)
answer = int(str(answer)[2])

for client in clients:
    if client["number"] == answer:
        os.system(f"hyprctl dispatch workspace {client['workspace']}")