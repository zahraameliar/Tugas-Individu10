"""
Nama : Zahra Amelia Ramadhani
NIM : 2501962
Kelas : 1A
"""

nilai = int(input("Masukkanlah Nilai: "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid, Masukin nilai yang benar")
elif nilai >= 90:
    print("Nilai: A")
elif nilai >= 80:
    print("Nilai: B")
elif nilai >= 70:
    print("Nilai: C")
else:
    print("Nilai: D")