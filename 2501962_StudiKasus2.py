"""
Nama : Zahra Amelia Ramadhani
NIM : 2501962
Kelas : 1A
"""


jenis_kelamin = input("Masukkan jenis kelamin (Wanita/Pria): ").lower()
umur = int(input("Masukkan Umur: "))
tinggi = int(input("Masukkan Tinggi badan (cm): "))
iq = int(input("Masukkan IQ: "))

if (18 <= umur <= 25) and (iq >= 130) and ((jenis_kelamin == "Wanita" and tinggi >= 170) or (jenis_kelamin == "Pria" and tinggi >= 175)):
    print("Yay! Kamu bisa menjadi seorang model catwalk")
else:
    print("Maaf kamu belum memenuhi syarat untuk menjadi model catwalk.")