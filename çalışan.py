# self -> ç1,ç2,ç3...

class Çalışan(): # Sınıf tanımlaması

    personel = [] # Eklenecek personeller için boş liste

    def __init__(self,isim): # Sınıf örneklemesi yapmak ve otomatik çalıştırmak için kullanılan fonksiyon 
        self.isim = isim 
        self.kabiliyetleri = []
        self.personele_ekle()

    @classmethod
    def personel_sayısını_görüntüle(cls): # Personel sayısını görüntülemek için kullanılan fonksiyon
        print(len(cls.personel))

    def personele_ekle(self): # Personel listesine çalışan eklemek için kullanılan fonksiyon
        self.personel.append(self.isim)
        print("{} adlı kişi personel listesine eklendi.".format(self.isim))

    @classmethod
    def personeli_görüntüle(cls): # Personellerin listesini görüntülemek için kullanılan fonksiyon
        print("Personel Listesi:")
        for personel in cls.personel:
            print(personel)

    def kabiliyet_ekle(self,kabiliyet): # Personellere kabiliyet eklemek için kullanılan fonksiyon
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self): # Personellerin kabiliyetlerini görüntülemek için kullanılan fonksiyon
        print("{} adlı personelin kabiliyetleri:".format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)