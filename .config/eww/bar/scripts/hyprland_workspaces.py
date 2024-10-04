import os
import json

home_dir = os.path.expanduser("~")
colors_path = os.path.join(home_dir, 'bin', 'colors.json')
with open(colors_path, 'r') as file:
    colors = json.load(file)

def hyprland_workspaces():
    return json.load(os.popen("hyprctl workspaces -j"))

def workspaces():
    spaces = list()
    for workspace in hyprland_workspaces():
        spaces.append({"id": workspace["id"], "name": workspace["name"]})
    return sorted(spaces, key=lambda spaces: spaces["id"])

def active_workspace():
    return json.load(os.popen("hyprctl activeworkspace -j"))["id"]

def main():
    spaces = workspaces()
    string = "(box :orientation 'v' :spacing 2 "

    for space in spaces:
        style = ""
        name = str(space["name"])
        id = space["id"]
        if space["name"] == "special:special":
            name = "S"
            style = ":css 'button {background: " + colors["colors"]["color1"] + "}'"
        if space["id"] == active_workspace():
            style = ":css 'button {background: " + colors["colors"]["color2"] + "}'"
        string += f"""(button {style} :onclick 'hyprctl dispatch workspace {id}' '{name}') """
    string += ")"

    print(string)


if __name__ == "__main__":
    main()
