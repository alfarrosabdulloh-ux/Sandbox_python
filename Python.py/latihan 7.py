 latihan 7
# ===== LATIHAN 1: Countdown Sederhana =====
print("\n=== Latihan 1: Countdown Sederhana ===")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blastoff!")

# ===== LATIHAN 2: Game Tebak Angka =====
print("\n=== Latihan 2: Game Tebak Angka ===")
angka_rahasia = 7

while True:
    try:
        tebakan = int(input("Tebak angka rahasia (1-10): "))
        if tebakan == angka_rahasia:
            print("Selamat, tebakan Anda benar!")
            break
        else:
            print("Salah, coba lagi!")
    except:
        print("Input tidak valid, harus angka!")

print("Terima kasih sudah bermain!")

# ===== LATIHAN 3: Input Angka Cerdas =====
print("\n=== Latihan 3: Input Angka Cerdas ===")
total = 0
count = 0

while True:
    data = input("Masukkan angka (atau ketik 'done' untuk selesai): ")
    if data.lower() == "done":
        break
    try:
        angka = float(data)
        total += angka
        count += 1
    except:
        print("Input tidak valid")
        continue

# Hitung rata-rata dan cetak hasil
if count > 0:
    rata_rata = total / count
    hasil = (
        "\n=== Hasil Input Angka Cerdas ===\n"
        f"Total: {total}\n"
        f"Jumlah angka yang dimasukkan: {count}\n"
        f"Rata-rata: {rata_rata}\n"
    )
    print(hasil)

    # Simpan ke file
    with open("hasil_input.txt", "w") as file:
        file.write(hasil)

    print("Hasil telah disimpan ke file 'hasil_input.txt'")
else:
    print("Tidak ada angka yang dimasukkan.")