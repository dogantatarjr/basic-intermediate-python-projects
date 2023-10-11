import time
import random
import sys

class Oyuncu(): # Sınıf tanımlaması
    def __init__(self,isim,can=5,enerji=100): # Özellikler
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji

    def mevcut_durumu_görüntüle(self): # Mevcut durumu görüntüleme
        print("Darbe:",self.darbe)
        print("Can:",self.can)
        print("Enerji:",self.enerji,"\n")
    
    def saldır(self,rakip): # Saldırı yapma
        print("Bir saldırı gerçekleştirdiniz.")
        print("Saldırı sürüyor. Bekleyiniz.")

        for i in range(10):
            time.sleep(.3)
            print(".",end="",flush=True)

        sonuç = self.saldırı_sonucunu_hesapla()

        if sonuç == 0:
            print("\nSONUÇ: Kazanan Taraf Yok\n")
        
        if sonuç == 1:
            print("\nSONUÇ: Rakibinizi Darbelediniz\n")
            self.darbele(rakip)
        
        if sonuç == 2:
            print("\nSONUÇ: Rakibinizden Darbe Aldınız\n")
            self.darbele(self)

    def saldırı_sonucunu_hesapla(self): # Saldırı sonucu hesaplama (Rastgele)
        return random.randint(0,2)
    
    def kaç(self): # Kaçma
        print("Kaçılıyor. Bekleyiniz.")
        for i in range(10):
            time.sleep(.3)
            print(".",end="",flush=True)
        
        print("\nRakibiniz Sizi Yakaladı")

    def darbele(self,darbelenen): # Darbe verme
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe / 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print("Oyunu {} kazandı!".format(self.isim))
            self.oyundan_çık()
    
    def oyundan_çık(self):
        print("Oyundan Çıkılıyor...")
        sys.exit()

#################################################################

# Oyuncular
siz = Oyuncu("Junior")
isim = "Junior"
darbe = 0
can = 5
enerji = 100

rakip = Oyuncu("PC")
isim = "PC"
darbe = 0
can = 5
enerji = 100

# Oyun Başlangıcı
while True:
    print("Şu anda rakibinizle karşı karşıyasınız.",
    "Yapmak istediğiniz hamle: ",
    "Saldır: s",
    "Kaç: k",
    "Oyundan Çık: q", sep="\n")

    hamle = input(">")

    if hamle == "s":
        siz.saldır(rakip)

        siz.saldırı_sonucunu_hesapla()

        print("Rakibinizin Durumu:")
        rakip.mevcut_durumu_görüntüle()

        print("Sizin Durumunuz:")
        siz.mevcut_durumu_görüntüle()

    if hamle == "k":
        siz.kaç()

    if hamle == "q":
        siz.oyundan_çık()