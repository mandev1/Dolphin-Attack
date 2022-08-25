# Dolphin-Attack
Source Code of Dolphin Attack code for Smart Speaker

## Pendahuluan
Pembajakan suara adalah metode hacking yang digunakan untuk
mengirimkan instruksi dengan perantara udara dan menggunakan gelombang
ultrasonik. Teknik ini disebut sebagai dolphin attack, karena cara
kerjanya sama seperti cara lumba-lumba untuk berkomunikasi dengan kawanannya.

## Cara Kerja
Dalam penelitian ini, terdapat komputer pengirim berlaku sebagai Command
and Control (CnC), mengirimkan instruksi menuju komputer yang dijadikan
perantara pengiriman instruksi ke smart speaker. CnC mengirimkan instruksi untuk
smart speaker dalam bentuk teks dan dikirimkan ke komputer target melalui socket.
Setelah komputer target telah menerima instruksi, dikonversi menjadi audible
audio, lalu dimodulasi menjadi inaudible audio dan diputar pada komputer target dan
didengarkan oleh smart speaker. Konsep cara kerja dari dolphin attack dapat dilihat
pada Gambar dibawah.

![image](https://user-images.githubusercontent.com/101856662/186618297-1ad98cb0-c41b-4c5f-9ac5-4a4c3a506df1.png)

## Source Code
Program server yang dimasukkan pada komputer target bertugas sebagai
perantara komputer target dan CnC untuk mengirimkan instruksi dan dikonversikan
menjadi gelombang suara ultrasonik. Program server bertugas untuk
mengkonversikan instruksi yang diberikan dari server untuk menjadi gelombang
ultrasonik dan dikeluarkan oleh loudspeaker komputer target. Saat program
dijalankan, server lalu mencari koneksi client lalu terhubung dan server siap
menerima instruksi dari client. 

### Client side
Setelah terhubung, client bisa mengirimkan instruksi dengan menggunakan
socket, diterima oleh server dan diproses pada komputer target. Cara kerja program
client dapat dilihat pada Gambar dibawah.

![image](https://user-images.githubusercontent.com/101856662/186618436-6fe0fde9-9d5e-4490-a615-d7d9a8d887ad.png)

### Server Side
Saat client mengirimkan instruksi, server menerima instruksi tersebut lalu
dikonversikan menjadi suara inaudible. Gelombang ultrasonik ini lalu dikeluarkan
oleh loudspeaker dan diterima oleh smart speaker. Cara kerja program server dapat
dilihat pada Gambar dibawah.

![image](https://user-images.githubusercontent.com/101856662/186618507-6d019d4a-4aa8-4953-ba4b-9c6a493b911c.png)
