import socket
import pyttsx3
from scipy import signal
from scipy.io import wavfile
import numpy as np
import os
import time
import matplotlib.pyplot as plt



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
        audio_duration = len(samples)/ sample_rate
        audio_time = np.arange(0, audio_duration, 1/sample_rate)

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

        audio_duration_new = len(voice_upsampling)/ 192000
        upsampling_time = np.arange(0, audio_duration_new, 1/192000)

        carrier_freq = 20000
        carrier_signal = np.sin(2 * np.pi * carrier_freq * upsampling_duration)
        ultrasound = (carrier_signal * voice_upsampling) + carrier_signal
        ultrasound_norm = ultrasound/np.amax(np.abs(ultrasound))


         # menyimpan sinyal am
        wavfile.write("am.wav", 192000, ultrasound_norm)
        os.system('start am.wav')

        # grafik Audio Asli     (data percobaan)
        plt.subplot(4, 1, 1)
        plt.title('Audio Data')
        plt.plot(audio_time, samples)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        #plt.show()

        # grafik LPF            (data percobaan)
        plt.subplot(4, 1, 2)
        plt.title('Filtered')
        plt.plot(audio_time, voice_filter)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        #plt.show()

        # Grafik upsampling     (data percobaan)

        plt.subplot(4, 1, 3)
        plt.title('Upsampling')
        plt.plot(upsampling_time, voice_upsampling)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        #plt.show()

        # grafik AM         (data percobaan)
        plt.subplot(4, 1, 4)
        plt.title('Ultrasonic')
        plt.plot(upsampling_time, ultrasound_norm)
        plt.ylabel('Amplitude')
        plt.xlabel('Time')
        plt.show()
    

        client.close()
