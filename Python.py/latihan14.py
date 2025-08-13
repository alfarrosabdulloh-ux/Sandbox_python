# latihan 1
# List kosong
belanjaan = []

# Menambahkan item dengan .append()
belanjaan.append("Telur")
belanjaan.append("Susu")
belanjaan.append("Roti")

# Menambahkan "Apel" di posisi awal
belanjaan.insert(0, "Apel")

# Menghapus "Susu"
belanjaan.remove("Susu")

# Cetak list akhir
print("Daftar belanjaan:", belanjaan)

# latihan 2
nilai = [98, 76, 88, 100, 54]

# sorted() mengembalikan list baru
nilai_terurut = sorted(nilai)

print("Nilai asli:", nilai)
print("Nilai terurut:", nilai_terurut)

# latihan 3
kalimat = input("Masukkan kalimat: ")

# Pisahkan jadi list kata
kata_list = kalimat.split()

# Hitung jumlah kata
print("Jumlah kata:", len(kata_list))

# Urutkan kata berdasarkan abjad
kata_list.sort()
print("Kata-kata terurut:", kata_list)

# latihan 4
a = [1, 2, 3, 4, 5]
b = a           # b adalah alias dari a (mengacu ke list yang sama)
c = a.copy()    # c adalah salinan baru (berbeda objek)

b[1] = 20       # Mengubah indeks ke-1 pada list a dan b
c[1] = 30       # Mengubah indeks ke-1 pada list c saja

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

