import ctypes
import os
username = os.getlogin()
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:\\users\\{username}\\AppData\\Local\\Aryan\\Badware\\wallpaper.png", 0)
#os.remove(f"C:\\users\\{username}\\AppData\\Local\\Aryan\\Badware\\wallpaper.png")