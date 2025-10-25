import os

def change_wallpaper(image_path="assets/grass.png"):
    command = f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}"
    os.system(command)

change_wallpaper(image_path=os.path.abspath("assets/grass.png"))