#coding: utf-8
import wave
import sys
import pyaudio
CHUNK = 1024
filename = "../Assets/Roundabout.wav"
wf = wave.open(filename,"rb")
print wf
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                #rate = 40000,
                output=True)
data = wf.readframes(CHUNK) 

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    
stream.stop_stream()
stream.close()

p.terminate()
