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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = socket.gethostbyname(socket.gethostname())
    port = 1234

    print(ip)

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

        time.sleep(5)
        # membaca data audio
        sample_rate, samples = wavfile.read("test.wav")
        duration = len(samples)/sample_rate
        audio_time = np.arange(0, duration, 1/sample_rate)

        # lowpass filter audio
        b, a = signal.butter(10, 2*4000/sample_rate, btype="low")
        voice_filter = signal.lfilter(b, a, samples)

        carrier_freq = 20000
        amplitude = 2
        carrier_signal = amplitude * np.sin(2 * np.pi * carrier_freq * audio_time)
        ultrasound = (carrier_signal * voice_filter)+ carrier_signal
        ultrasound_norm = ultrasound/np.amax(np.abs(ultrasound))

    # menyimpan sinyal am
        wavfile.write("am.wav", sample_rate, ultrasound_norm)
        os.system('start am.wav')

        # grafik Audio Asli     (data percobaan)
        plt.subplot(4, 1, 1)
        plt.title('Audio Data')
        plt.plot(audio_time, samples)
        plt.ylabel('Amplitude')
        #plt.xlabel('Time')
        #plt.show()

        # grafik LPF            (data percobaan)
        plt.subplot(4, 1, 2)
        plt.title('Filtered')
        plt.plot(audio_time, voice_filter)
        plt.ylabel('Amplitude')
        #plt.xlabel('Time')
        #plt.show()


        # grafik AM         (data percobaan)
        plt.subplot(4, 1, 3)
        plt.title('Ultrasonic')
        plt.plot(audio_time, ultrasound_norm)
        plt.ylabel('Amplitude')
        plt.xlabel('Time')
        plt.show()
