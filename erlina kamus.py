my_dict={'saya':'kaji','kamu':'sia','mandi':'maneng','makan':'mangan','tidur':'tunung'}


print(""" 
             KAMUS BAHASA SUMBAWA
=================================================""")

artinya=input("Masukkan kata yang ingin anda terjemahkan : ")


if artinya=='saya':
    print(f"Saya : {my_dict['saya']}")
elif artinya=='kamu':
    print(f"Kamu : {my_dict['kamu']}")
elif artinya =='mandi': 
    print(f"Mandi : {my_dict['mandi']}")
elif artinya=='makan':
    print(f"Makan : {my_dict['makan']}")
elif artinya=='tidur':
    print(f"Tidur : {my_dict['tidur']}")
else:
    print("KATA YANG ANDA MASUKAN TIDAK FALID")
            
