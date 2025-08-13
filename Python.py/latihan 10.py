# latihan 10.py
#1
judul = input("Masukkan judul buku: ")
judul_bersih = judul.strip().title()
print("Judul standar:", judul_bersih)

#2
email = input("Masukkan email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")

#3
kalimat = "Harga tiketnya sangat mahal."
kata_sensor = "mahal"

kalimat_disensor = kalimat.replace(kata_sensor, "***")
print(kalimat_disensor)

#4
organisasi = input("Masukkan nama organisasi: ")

kata_kata = organisasi.split()
akronim = ""

for kata in kata_kata:
    akronim += kata[0].upper()

print("Akronim:", akronim)

#5
import re

judul_artikel = input("Masukkan judul artikel: ")
judul_lower = judul_artikel.lower()
judul_slug = re.sub(r'[^a-z0-9\s-]', '', judul_lower)  # hapus simbol
slug = "-".join(judul_slug.split())  # ganti spasi dengan '-'

print("Slug URL:", slug)
