# Latihan 1: Membuat dan Mengakses
jadwal_senin = ["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]

# Cetak seluruh list
print("Seluruh list:", jadwal_senin)

# Cetak mata pelajaran pertama
print("Mata pelajaran pertama:", jadwal_senin[0])

# Cetak mata pelajaran terakhir (indeks negatif)
print("Mata pelajaran terakhir:", jadwal_senin[-1])

print("-" * 40)

# Latihan 2: Modifikasi List
# Ubah "Olahraga" menjadi "Kimia"
jadwal_senin[2] = "Kimia"

# Cetak list setelah diperbarui
print("Jadwal Senin setelah diperbarui:", jadwal_senin)

print("-" * 40)

# Latihan 3: Traversing dan Modifikasi
nilai_mentah = [55, 63, 72, 81, 90]

# Tambahkan 5 ke setiap nilai
for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5

print("Nilai setelah bonus:", nilai_mentah)

print("-" * 40)

# Latihan 4: Slicing dan Penggabungan
awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]

# Gabungkan list
seminggu = awal_minggu + akhir_minggu

# Ambil hari kerja (Senin sampai Jumat)
hari_kerja = seminggu[0:5]

print("Hari kerja:", hari_kerja)
