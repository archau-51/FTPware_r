
import os
from gtts import gTTS
from playsound import playsound
import sys
username=os.getlogin
gTTS(text=sys.argv[1], lang="en", slow=False).save(fr'C:\users\{username}\AppData\local\Aryan\Badware\say.mp3')
playsound(fr'C:\users\{username}\AppData\local\Aryan\Badware\say.mp3')
os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\say.mp3')