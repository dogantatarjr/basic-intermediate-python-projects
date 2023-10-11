import os
import time

def clear():
    os.system('cls')

sekil = input("Hangi geometrik şeklin alanını bulmak istiyorsun ? (Kare, Dikdörtgen, Paralelkenar, Daire, Yamuk): ")
cevap = sekil.title()

clear()
time.sleep(1)

if cevap == "Kare": 
    kare_kenar = int(input("Karenin bir kenar uzunluğunu giriniz (br): "))
    kare_alan = int(kare_kenar * kare_kenar)

    clear()
    time.sleep(1)

    print("Karenin Alanı (br2):" , kare_alan , "br2")


if cevap == "Dikdörtgen":
    dikdortgen_uzun_kenar = int(input("Dikdörtgenin uzun kenarının uzunluğunu giriniz (br): "))
    dikdortgen_kisa_kenar = int(input("Dikdörtgenin kısa kenarının uzunluğunu giriniz (br): "))
    dikdortgen_alan = int(dikdortgen_kisa_kenar * dikdortgen_uzun_kenar)

    clear()
    time.sleep(1) 

    print("Dikdörtgenin Alanı (br2):" , dikdortgen_alan , "br2")


if cevap == "Paralelkenar":
    paralelkenar_taban = int(input("Paralelkenarın taban uzunluğunu giriniz (br): "))
    paralelkenar_yukseklik = int(input("Paralelkenarın yüksekliğini giriniz (br): "))
    paralelkenar_alan = int(paralelkenar_taban * paralelkenar_yukseklik)

    clear()
    time.sleep(1)

    print("Paralelkenarın Alanı (br2):" , paralelkenar_alan , "br2")


if cevap == "Daire":
    daire_yarıcap = int(input("Dairenin yarıçapını giriniz (br): "))
    daire_alan = int((daire_yarıcap * daire_yarıcap) * 3)

    clear()
    time.sleep(1)

    print("Dairenin Alanı (br2):" , daire_alan , "br2")


if cevap == "Yamuk":
    yamuk_taban = int(input("Yamuğun taban uzunuluğunu giriniz (br): "))
    yamuk_tavan = int(input("Yamuğun tavan uzunluğunu giriniz (br): "))
    yamuk_yukseklik = int(input("Yamuğun yüksekliğini giriniz (br): "))
    yamuk_alan = int(((yamuk_taban + yamuk_tavan) * yamuk_yukseklik) / 2)

    clear()
    time.sleep(1)

    print("Yamuğun Alanı (br2):" , yamuk_alan , "br2")