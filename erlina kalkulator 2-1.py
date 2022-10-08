print("Kalkulator Sederhana Python\n")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Exit")

print("\nnote:Jika anda memilih 5. Exit maka anda akan keluar dari program!")
pilihan=int(input("\nMasukan Pilihan Operasi : "))


if pilihan == 1:
    bilangan1= float(input("Bilangan 1 : "))
    bilangan2= float(input("Bilangan 2 : "))
    print(f"{bilangan1} + {bilangan2} = {bilangan1+bilangan2}")
elif pilihan == 2:
    bilangan1= float(input("Bilangan 1 : "))
    bilangan2= float(input("Bilangan 2 : "))
    print(f"{bilangan1} - {bilangan2} = {bilangan1-bilangan2}")
elif pilihan == 3:
    bilangan1= float(input("Bilangan 1 : "))
    bilangan2= float(input("Bilangan 2 : "))
    print(f"{bilangan1} * {bilangan2} = {bilangan1*bilangan2}")
elif pilihan == 4:
    bilangan1=float(input("Bilangan 1: "))
    bilangan2=float(input("Bilangan 2: "))
    print(f"{bilangan1} / {bilangan2} = {bilangan1/bilangan2}")
elif pilihan == 0:
    print("Program Keluar")
else:
    print("Perintah tidak dikenal")
    print("Anda telah 'Keliar' dari Program")