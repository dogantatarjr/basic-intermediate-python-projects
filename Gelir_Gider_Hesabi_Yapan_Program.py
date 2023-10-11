import time
import os

def clear():
    os.system('cls')

print("""
---------------------------------------
 Gelir-Gider Hesaplama Tablosu (Aylık)
---------------------------------------
""")

print(""" 
Gelirler:
----------
""")

maas = int(input("Maaş (TL): "))
harclik = int(input("Harçlık (TL): "))
ek_gelir = int(input("Ek Gelir (TL): "))
burs = int(input("Burs Geliri (TL): "))
staj = int(input("Staj Geliri (TL): "))
kira_gelir = int(input("Kira Geliri (TL): "))

print(""" 
Giderler:
----------
""")

kira = int(input("Kira (TL): "))
yemek = int(input("Yemek/Market (TL): "))
faturalar = int(input("Faturalar (TL): "))
emlak = int(input("Emlak Vergisi (TL): "))
aidat = int(input("Aidat (TL): "))
borc = int(input("Borçlar/Taksitler (TL): "))
kisisel = int(input("Kişisel Harcamalar (TL): "))

clear()
time.sleep(0.5)
print("Gelir-Gider Hesaplaması Yapılıyor... ")
time.sleep(2)
clear()

toplam_gelir = int(maas + harclik + ek_gelir + burs + staj + kira_gelir)
toplam_gider = int(kira + yemek + faturalar + emlak + aidat + borc + kisisel)
gelir_gider = int(toplam_gelir - toplam_gider)

print("""
Sonuç
------""")

if gelir_gider < 0:
    print("Zarar Miktarı: " , gelir_gider)
    print("Daha Tasarruflu Olmalısın !!!")

if gelir_gider > 0:
    print("Kar Miktarı: " , gelir_gider)
    if gelir_gider > 100:
        print("Güzel Tasarruf Yapmışsın :)")
    elif gelir_gider < 100:
        print("Daha Fazla Tasarruf Yapabilirsin Ama Bu Da İyi :)")