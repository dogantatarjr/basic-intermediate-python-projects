sayi1 = int(input("Bir Sayı Giriniz: "))
islem = input("Yapmak İstediğiniz İşlemi Giriniz (+,-,*,/): ")
sayi2 = int(input("İkinci Bir Sayı Giriniz: "))

if islem == "+": 
    print("İşleminizin Sonucu:" , sayi1 + sayi2)
if islem == "-":
    print("İşleminizin Sonucu:" , sayi1 - sayi2)
if islem == "*":
    print("İşleminizin Sonucu:" , sayi1 * sayi2)
if islem == "/":
    print("İşleminizin Sonucu:" , sayi1 / sayi2)