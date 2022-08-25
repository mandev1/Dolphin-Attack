import socket
import pyttsx3
from scipy import signal
from scipy.io import wavfile
import numpy as np
import os




class TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,string):
        self.engine.save_to_file(string, "test.wav")
        self.engine.runAndWait()


if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    port = 1234
    print(ip)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)

    while True:
        client, address = s.accept()
        print(f"Connection Estabished - {address[0]}:{address[1]}")
        string = client.recv(1024)
        string = string.decode("utf-8")
        print(string)
        
        tts = TTS()
        tts.start(string)
        del(tts)

        # membaca data audio
        sample_rate, samples = wavfile.read("test.wav")

        # lowpass filter audio
        b, a = signal.butter(10, 2*4000/sample_rate, btype="low")
        voice_filter = signal.lfilter(b, a, samples)

        # upsampling audio
        order = int(len(voice_filter)*192000/sample_rate)
        voice_upsampling = signal.resample(voice_filter, order)


        # modulasi AM
        dt = 1/192000
        size = voice_upsampling.shape[1 -1]
        upsampling_duration = np.transpose((np.arange(0, (size - 1) * dt+dt, dt)))

        carrier_freq = 20000
        carrier_signal = np.sin(2 * np.pi * carrier_freq * upsampling_duration)
        ultrasound = (carrier_signal * voice_upsampling) + carrier_signal
        ultrasound_norm = ultrasound/np.amax(np.abs(ultrasound))


         # menyimpan sinyal am
        wavfile.write("am.wav", 192000, ultrasound_norm)
        os.system('start am.wav')
        client.close()
