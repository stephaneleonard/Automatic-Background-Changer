import ctypes

def updateBackground():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/stefl/Documents/Automatic-Background-Changer/sample_image.png" , 0)