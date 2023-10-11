class Sorgu(): # Sınıf tanımlaması

    def __init__(self,değer=None,sıra=None):
        self.liste = [("7852369741256","Heather McCollum","Şahane Hatalar 1","April"),
        ("1287469852351","Jane Hellberg","Katil Balina","Andromeda"), # Kitap listesi (Veri Tabanı kullanılacak)
        ("7416934268711","William Junior","Bira ve Kadın","April"),] 

        if not değer and not sıra:
            l = self.liste
        else:
            l = [li for li in self.liste if değer == li[sıra]]              # Yazdırılacak yazının düzenlemesi

        for i in l:
            print(*i, sep=", ")
        
    @classmethod
    def isbnden(cls, isbn): # ISBN numarasından sorgulama
        cls(isbn, 0)
    @classmethod
    def yazardan(cls, yazar): # Yazar adından sorgulama
        cls(yazar, 1)
    @classmethod
    def eserden(cls, eser): # Eser adından sorgulama
        cls(eser, 2)
    @classmethod
    def yayınevinden(cls, yayınevi): # Yayınevinden sorgulama
        cls(yayınevi, 3)