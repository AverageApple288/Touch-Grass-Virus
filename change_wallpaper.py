import os

def change_wallpaper(image_path="assets/grass.png"):
    command_gnome = f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}"
    os.system(command_gnome)
    command_hyprland = f"swww img {image_path}"
    os.system(command_hyprland)

change_wallpaper(image_path=os.path.abspath("assets/grass.png"))