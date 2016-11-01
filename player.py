import pyaudio
import wave
import time

class AudioPlayer:

    def __init__(self):
        self.p = pyaudio.PyAudio()

    def callback(self,in_data,frame_count,time_info,status):
        data = self.wf.readframes(frame_count)
        return (data,pyaudio.paContinue)

    def playWav(self,filename):
        self.wf = wave.open(filename,'rb')
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                channels=self.wf.getnchannels(),
                                rate = self.wf.getframerate(),
                                output=True,
                                stream_callback=self.callback)
        self.stream.start_stream()
        #self.stream.stop_stream()
        #self.stream.close()
        #self.wf.close()
    
    def pause(self):
        self.stream.stop_stream()
    
    def resume(self):
        self.stream.start_stream()
        
#self.p.terminate()

