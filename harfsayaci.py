class HarfSayacı: # Sınıf tanımlaması
    
    def __init__(self): # Sesli-sessiz harfleri tanımlama ve sayaç tanımlama için kullanılan fonksiyon
        self.sesli_harfler = "aeıioöuü"
        self.sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    def kelime_sor(self): # Kelime girşi
        return input("Bir kelime girin: ")

    def seslidir(self,harf): # Sesli harf sorgulama
        return harf in self.sesli_harfler

    def sessizdir(self,harf): # Sessiz harf sorgulama
        return harf in self.sessiz_harfler

    def artır(self): # Sesli ve sessiz harfleri sayaca ekleme
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli+=1
            if self.sessizdir(harf):
                self.sayaç_sessiz+=1
        return (self.sayaç_sesli,self.sayaç_sessiz)

    def ekrana_bas(self): # Mesaj yazdırma
        sesli,sessiz = self.artır()
        mesaj = "{} kelimesinde {} sesli, {} sessiz harf vardır."
        print(mesaj.format(self.kelime,sesli,sessiz))

    def çalıştır(self): # Programı çalıştırma
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == "__main__": # REPL'da çalıştırma
    sayaç = HarfSayacı()
    sayaç.çalıştır()