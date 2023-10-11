from random import randint
import time
import os

def clear():
    os.system('cls')

while True:
    rand = randint(1,11)
    sayi = int(input("1 ile 10 arasında bir sayı gir bakalım: "))

    if sayi == rand:
        print("Vaay! Aklımda tuttuğum sayıyı bildin! Helal Olsun!")

    elif sayi > 10 or sayi <= 0:
        print("Sana 1 ile 10 arasında bir sayı gir demiştim!")

    else:
        print("Bilemedin! Nabbeeeer! Doğru Cevabı da Göstereyim de Mereklanma :D Cevap:" , rand)

    time.sleep(1)

    soru = input("Bir Daha Oynamak İster Misin ?: ")

    cevap = soru.title()

    if cevap == "Evet":
        clear()
    
    if cevap == "Hayır":
        clear()
        time.sleep(1)
        print("Oynadığın İçin Teşekkürler !")
        break