import os

print("""
Selamat datang di GAME TEBAK NAMA SEDERHANA 
**>*************************************<**\n
Daftar nama : Septi, Bayu, Budi, Tono, Dika, Danu, Anto, Elga, Safi

PLAYER 1: Masukkan nama yang akan ditebak oleh PLAYER 2 berdasarkan dari ketentuan diatas! \n
""")
rahasia=str(input("Masukkan nama rahasia yang akan di tebak oleh player 2 : "))
os.system('cls')

print("""PLAYER 1 sudah membuat nama yang akan ditebak, PLAYER 2 silahkan menebak :""")
batas=3
for coba in range(batas):
    jawab=str(input(f"Masukkan nama tebakan PLAYER 2 : "))
    if jawab == rahasia:
        print("Selamat, tebakan anda Benar!")
        break
    else:
        print(f"Coba lagi...\nyuk masih kesisa {coba+1}x tebakan lagi.")
if coba == batas-1:

    print("Duhh... ZONKK")