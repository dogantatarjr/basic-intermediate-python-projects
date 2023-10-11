ad = input("Öğrencinin adını giriniz: ")
soyad = input("Öğrencinin soyadını giriniz: ")

bir = input("Öğrencinin ilk sınav notunu giriniz: ")
iki = input("Öğrencinin ikinci sınav notunu giriniz: ")
uc = input("Öğrencinin üçüncü sınav notunu giriniz: ")
ortalama = round((int(bir)+int(iki)+int(uc))/3)
gecti = "sınıfı geçmiştir"
kaldi = "sınıfta kalmıştır"

sinavnot = "{} {} adlı öğrencinin ilk sınav notu {}, ikinci sınav notu {}, üçüncü sınav notu {}, dönem ortalaması {}. Öğrenci {}." # Karne Notu Cümlesinin Değişkeni

if ortalama > 100:
    print("Geçerli bir değer giriniz !")

elif ortalama >= 50:
    print(sinavnot.format(ad,soyad,bir,iki,uc,ortalama,gecti))

elif ortalama < 50:
    print(sinavnot.format(ad,soyad,bir,iki,uc,ortalama,kaldi))