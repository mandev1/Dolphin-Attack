# Dolphin-Attack
Source Code of Dolphin Attack code for Smart Speaker

Pembajakan suara adalah metode hacking yang digunakan untuk
mengirimkan instruksi dengan perantara udara dan menggunakan gelombang
ultrasonik. Teknik ini disebut sebagai dolphin attack, karena cara
kerjanya sama seperti cara lumba-lumba untuk berkomunikasi dengan kawanannya.

Dalam penelitian ini, terdapat komputer pengirim berlaku sebagai Command
and Control (CnC), mengirimkan instruksi menuju komputer yang dijadikan
perantara pengiriman instruksi ke smart speaker. CnC mengirimkan instruksi untuk
smart speaker dalam bentuk teks dan dikirimkan ke komputer target melalui socket.
Setelah komputer target telah menerima instruksi, dikonversi menjadi audible
audio, lalu dimodulasi menjadi inaudible audio dan diputar pada komputer target dan
didengarkan oleh smart speaker. Konsep cara kerja dari dolphin attack dapat dilihat
pada Gambar 3.1.

Program server yang dimasukkan pada komputer target bertugas sebagai
perantara komputer target dan CnC untuk mengirimkan instruksi dan dikonversikan
menjadi gelombang suara ultrasonik. Program server bertugas untuk
mengkonversikan instruksi yang diberikan dari server untuk menjadi gelombang
ultrasonik dan dikeluarkan oleh loudspeaker komputer target. Saat program
dijalankan, server lalu mencari koneksi client lalu terhubung dan server siap
menerima instruksi dari client.
Setelah terhubung, client bisa mengirimkan instruksi dengan menggunakan
socket, diterima oleh server dan diproses pada komputer target. Cara kerja program
client dapat dilihat pada Gambar 3.3.

Saat client mengirimkan instruksi, server menerima instruksi tersebut lalu
dikonversikan menjadi suara inaudible. Gelombang ultrasonik ini lalu dikeluarkan
oleh loudspeaker dan diterima oleh smart speaker. Cara kerja program server dapat
dilihat pada Gambar 3.4.
