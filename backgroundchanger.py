def download_image(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        print(f"Image downloaded to {path}")
        return path
    except Exception as e:
        raise RuntimeError(f"Error downloading image: {str(e)}") from e

def find_xfce_property():
    try:
        user = os.environ.get("USER")
        dbus_address_cmd = f'cat /proc/$(pgrep -u {user} xfce4-session)/environ | tr "\\0" "\\n" | grep DBUS_SESSION_BUS_ADDRESS | cut -d= -f2-'
        dbus_address = subprocess.check_output(["/bin/bash", "-c", dbus_address_cmd]).strip().decode("utf-8")
        os.environ["DBUS_SESSION_BUS_ADDRESS"] = dbus_address
        
        properties = subprocess.check_output(["xfconf-query", "-c", "xfce4-desktop", "-l"]).decode("utf-8").split("\n")
        
        for prop in properties:
            if "last-image" in prop:
                return prop
        raise ValueError("No suitable property path found.")
    except Exception as e:
        raise RuntimeError(f"Error finding XFCE property: {str(e)}") from e

def set_xfce_wallpaper(image_path):
    try:
        property_path = find_xfce_property()
        subprocess.run(["xfconf-query", "-c", "xfce4-desktop", "-p", property_path, "-s", f"{image_path}"], check=True)
        print(f"XFCE: Wallpaper changed to {image_path}")
    except Exception as e:
        print(f"XFCE: Failed to set wallpaper. Error: {str(e)}")

def file_uri(file_path):
    return "file://" + quote(file_path)

def set_gnome_wallpaper(image_path):
    try:
        print(f"GNOME: Changing wallpaper to {image_path}")
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", file_uri(image_path)], check=True)
        print(f"GNOME: Wallpaper changed to {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"GNOME: Failed to set wallpaper. Error: {str(e)}")

def change_wallpaper(image_path):
    try:
        if not os.path.exists(image_path):
            print(f"No image found at {image_path}")
            return
        
        image_path = os.path.abspath(image_path)

        desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
        if "gnome" in desktop_env:
            set_gnome_wallpaper(image_path)
        elif "xfce" in desktop_env:
            set_xfce_wallpaper(image_path)
        else:
            print("Unsupported desktop environment")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace with the desired URL and download path
image_url = "https://pbs.twimg.com/media/EYUgEFkWsAE-Tkg?format=jpg&name=4096x4096"
download_path = "wallpaper.jpg"

image_path = download_image(image_url, download_path)
change_wallpaper(image_path)
