# Latihan 1
filename = input("Masukkan nama file: ")

try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.upper().rstrip())
except FileNotFoundError:
    print(f"File '{filename}' tidak ditemukan.")

    # Latihan 2
filename = input("Masukkan nama file: ")

try:
    with open(filename, 'r') as file:
        total = 0
        count = 0
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                number = float(line[len("X-DSPAM-Confidence:"):].strip())
                total += number
                count += 1
        if count > 0:
            print("Rata-rata spam confidence:", total / count)
        else:
            print("Tidak ditemukan baris dengan 'X-DSPAM-Confidence:'.")
except FileNotFoundError:
    print(f"File '{filename}' tidak ditemukan.")

    # Latihan 3
filename = input("Masukkan nama file: ")

if filename.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.upper().rstrip())
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")