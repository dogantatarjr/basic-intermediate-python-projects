import random
import os

def clear():
    os.system('cls')

while True:
    print("-" * 35)

    print("Taş-Kağıt-Makas Oyununa Hoşgeldin !")
    
    print("-" * 35)

    secim = input("Seçimini Yap. Taş mı, Kağıt mı, Makas mı ?: ")
    secenek = ["Taş" , "Kağıt" , "Makas"]
    secim2 = secim.title()
    pc = random.choice(secenek)

    print("-" * 35)

    if secim2 == secenek[0]:
        if pc == secenek[2]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Kazandın !")
        if pc == secenek[1]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Kaybettin :(")
        if pc == secenek[0]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Berabere")

    if secim2 == secenek[1]:
        if pc == secenek[0]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Kazandın !")
        if pc == secenek[2]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Kaybettin :(")
        if pc == secenek[1]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Berabere")

    if secim2 == secenek[2]:
        if pc == secenek[1]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Kazandın !")
        if pc == secenek[0]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Kaybettin :(")
        if pc == secenek[2]:
            print("Senin Seçimin:" , secim2 + "\nBilgisayarın Seçimi:" , pc + "\nSonuç: Berabere")
    
    print("-" * 35)
    
    soru = input("Bir Daha Oynamak İster Misin ?: ")

    cevap = soru.title()

    if cevap == "Evet":
        clear()
    
    if cevap == "Hayır":
        clear()
        print("-" * 35)
        print("Oynadığın İçin Teşekkürler !")
        print("-" * 35)
        break