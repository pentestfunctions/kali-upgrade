# kali-upgrade

Don't run this garbage, just resetting my windows so threw it on here in the mean time. 

First run the removecrap.py file

Then you will want to install gnome
# Time to install gnome:
```sh
sudo apt-get update
sudo apt install gnome -y (Gives popups, will find way to automate)
sudo update-alternatives --config x-session-manager
```

- Restart your system after

- Then you will want to run the backgroundchanger.py file

After this install these customizations
https://extensions.gnome.org/extension/906/sound-output-device-chooser
https://extensions.gnome.org/extension/104/netspeed
https://extensions.gnome.org/extension/4679/burn-my-windows/
https://extensions.gnome.org/extension/3628/arcmenu/
Disable gnome system menu
In Dash to Panel Disable Show Applications Button

Search extensions in your machine and click settings for Burn my windows, choose the animation you want.

Install discord
```sh
wget "https://dl.discordapp.net/apps/linux/0.0.31/discord-0.0.31.deb"
sudo dpkg -i discord-0.0.31.deb
```

Install Brave Browser
```sh
sudo apt install curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install brave-browser
```
unpin firefox
pin bravebrowser to dash

Install gedit
```sh
sudo apt-get install gedit
xdg-mime default org.gnome.gedit.desktop text/plain
```
Add nautilus
```sh
sudo apt-get install nautilus
```
Install visual studio code
https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64
```sh
sudo dpkg -i "code_*"
```

Suru icons
```sh
sudo apt-get install meson
wget https://github.com/snwh/suru-icon-theme.git
cd suru-icon-theme
meson "build" --prefix=/usr
sudo ninja -C "build" install
gsettings set org.gnome.desktop.interface icon-theme "Suru"
```

```sh
sudo apt-get install konsole
```
pin to dash menu - remove terminal

Change profile picture
```sh
sudo nano /var/lib/AccountsService/users/kali
```
