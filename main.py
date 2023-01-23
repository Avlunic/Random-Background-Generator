
import requests
import urllib
import os

def updateBackground(file_path):

    #Updates the background
    os.system("/usr/bin/killall Dock")
    os.system("osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + file_path + "\" '")

    #Removes the remaining file
    try:
        os.remove("/Users/" + user + "/Desktop/currentImage.png")
    except:
        print("File error")

def grabRandomImage(user):

    #Grabs the image from picsum.photos (ALL IMAGE CREDIT GOES TO THEM)
    image = requests.get("https://picsum.photos/1920/1080.jpg")
    with open(r"/Users/" + user + "/Desktop/currentImage.png", "wb") as f:
        f.write(image.content)

    #Calls the update background function
    updateBackground("/Users/" + user + "/Desktop/currentImage.png")

user = str(os.popen("id -un").read()).strip()
grabRandomImage(user)