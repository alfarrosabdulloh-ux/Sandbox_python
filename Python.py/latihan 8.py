# latihan 8
# 1
for i in range(0, 71, 7):
    print(i)

# 2
kalimat = "Python"
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik

print(kalimat_terbalik)  # Output: "nohtyP"

#3
count = 0

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print("Jumlah angka yang habis dibagi 3 dan 5:", count)

#4
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()  # Pindah ke baris berikutnya

#5
n = int(input("Masukkan bilangan bulat positif: "))
hasil_faktorial = 1

for i in range(1, n + 1):
    hasil_faktorial *= i

print(f"Faktorial dari {n} adalah {hasil_faktorial}")