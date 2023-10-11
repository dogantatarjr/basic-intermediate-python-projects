dik = int(input("Üçgenin Dik Kenarının Uzunluğunu Giriniz (Birim): "))
yatay = int(input("Üçgenin Yatay Kenarının Uzunluğunu Giriniz (Birim): "))

from math import sqrt

hipo = sqrt(dik*dik + yatay*yatay)
cevre = hipo + dik + yatay
alan = yatay * dik / 2

print("Üçgenin Çevresi (Birim): " , cevre)
print("Üçgenin Alanı (Birim): " , alan)
print("Hipotenüs (Birim): " , hipo)