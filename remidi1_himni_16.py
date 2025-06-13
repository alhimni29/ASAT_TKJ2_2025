# remidi1_MuhammadAlHimniRusdi_16.py

bilangan = []

for i in range(1, 6):
    angka = int(input(f"Masukkan bilangan ke-{i}: "))
    bilangan.append(angka)

jumlah_genap = 0
for angka in bilangan:
    if angka % 2 == 0:
        jumlah_genap += 1

print(f"\nJumlah bilangan genap: {jumlah_genap}")
