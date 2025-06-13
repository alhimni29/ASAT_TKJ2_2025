# remidi2_MuhammadAlHimniRusdi_16.py

def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(r):
    return 3.14 * r * r

print("Pilih Menu:")
print("1. Luas Persegi")
print("2. Luas Lingkaran")

pilihan = int(input("\nPilihan Anda: "))

if pilihan == 1:
    sisi = float(input("Masukkan sisi: "))
    luas = luas_persegi(sisi)
    print(f"\nLuas persegi dengan sisi {sisi} adalah {luas}")
elif pilihan == 2:
    jari = float(input("Masukkan jari-jari: "))
    luas = luas_lingkaran(jari)
    print(f"\nLuas lingkaran dengan jari-jari {jari} adalah {luas}")
else:
    print("\nPilihan tidak tersedia.")
