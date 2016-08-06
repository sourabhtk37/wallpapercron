DIR="/home/sourabh/Downloads/wallpaper"

# Command to Select a random jpg file from directory
# Delete the *.jpg to select any file but it may return a folder

PIC=$(ls $DIR/*.jpg | shuf -n1)

# Command to set Background Image
#gconftool -t string -s /desktop/gnome/background/picture_filename $PIC
gsettings set org.gnome.desktop.background picture-uri $PIC