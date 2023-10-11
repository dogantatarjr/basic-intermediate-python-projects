class BuyuKKucukUnlu():
    def __init__(self):
        self.kalın = "aıouAIOU" 
        self.ince = "eiöüEİÖÜ"
        self.duz = "aeıiAEIİ"
        self.yuvarlak = "oöuüOÖUÜ"
        self.duz_genis = "aeAE"
        self.dar_yuvarlak = "uüUÜ"

    # Büyük ünlü uyumu
    def kalındır(self,harf):
        return harf in self.kalın
    def incedir(self,harf):
        return harf in self.ince

    #Küçük ünlü uyumu
    def düzdür(self,harf):
        return harf in self.duz
    def yuvarlaktır(self,harf):
        return harf in self.yuvarlak 
    def düz_geniştir(self,harf):
        return harf in self.duz_genis
    def dar_yuvarlaktır(self,harf):
        return harf in self.dar_yuvarlak

    def kelime_sor(self):
        self.kelime = str(input("Bir kelime giriniz: ")).title()

    def büyük_uyumu_yazdır(self,harf):
        if self.kalındır(harf) or self.incedir(harf) == True:
            print("{} kelimesi büyük ünlü uyumuna uymaktadır.".format(self.kelime))
        else:
            print("{} kelimesi büyük ünlü uyumuna uymamaktadır.".format(self.kelime))
    def küçük_uyumu_yazdır(self,harf):
        if self.düzdür(harf) or self.düz_geniştir(harf) or self.dar_yuvarlaktır(harf) == True:
            print("{} kelimesi küçük ünlü uyumuna uymaktadır.".format(self.kelime))
        else:
            print("{} kelimesi büyük ünlü uyumuna uymamaktadır.".format(self.kelime))

    def ekrana_bas(self):
        self.büyük_uyumu_yazdır(self.kelime)
        self.küçük_uyumu_yazdır(self.kelime)

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == "__main__":
    buku = BuyuKKucukUnlu()
    buku.çalıştır()