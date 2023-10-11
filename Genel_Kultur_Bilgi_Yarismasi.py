import time
import os

def clear():
    os.system('cls')

puan = 0

print("""------------------------------
 Genel Kültür Bilgi Yarışması
-------------------------------""")


print("Soru 1: Avusturlaya'nın Başkenti Neresidir ?")
print("""A) Sidney
B) Canberra
C) Oslo
D) Monaco
""")

cevap1 = input("Cevap: ")
cevap1_title = cevap1.title()

if cevap1_title == "B":
    puan += 20

clear()
time.sleep(1)


print("Soru 2: Amerika ve Rusya Arası Kaç Kilometredir ?")
print("""A) 3,2
B) 17.000
C) 5.000
D) 50.000
""")

cevap2 = input("Cevap: ")
cevap2_title = cevap2.title()

if cevap1_title == "A":
    puan += 20

clear()
time.sleep(1)


print("Soru 3: Dünyanın En Uzun İnsanı Kaç Metredir ?")
print("""A) 4,22
B) 2,80
C) 3,15
D) 2,51
""")

cevap3 = input("Cevap: ")
cevap3_title = cevap3.title()

if cevap1_title == "D":
    puan += 20

clear()
time.sleep(1)


print("Soru 4: Yetişkin Bir İnsanın Bedeninde Kaç Adet Kemik Vardır ?")
print("""A) 704
B) 320
C) 206
D) 150
""")

cevap4 = input("Cevap: ")
cevap4_title = cevap4.title()

if cevap1_title == "C":
    puan += 20

clear()
time.sleep(1)


print("Soru 5: Güneş Sisteminde Yüzey Sıcaklığı En Yüksek Olan Gezegen Hangisidir ?")
print("""A) Venüs
B) Mars
C) Plüton
D) Merkür
""")

cevap5 = input("Cevap: ")
cevap5_title = cevap5.title()

if cevap1_title == "A":
    puan += 20

clear()
time.sleep(1)


print("Toplam Puan: " , puan)

if puan == 0:
    print("Genel Kültür Seviyeniz: Çok Az")

elif puan < 60:
    print("Genel Kültür Seviyeniz: Az")

if puan == 60:
    print("Genel Kültür Seviyeniz: Orta")

elif puan == 100:
    print("Genel Kültür Seviyeniz: Çok Fazla")

elif puan > 60:
    print("Genel Kültür Seviyeniz: Fazla")