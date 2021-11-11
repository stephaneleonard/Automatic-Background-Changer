"""Change background"""
import ctypes
import os

def update_background(system):
    """Change background"""
    if system == 'Windows':
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/stefl/Documents/Automatic-Background-Changer/sample_image.png", 0)
    elif system == 'Linux':
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/stephane/Documents/projet\ perso/Automatic-Background-Changer/sample_image.png")
