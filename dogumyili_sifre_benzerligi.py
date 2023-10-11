import time
import os

def clear():
    os.system('cls')

print("Doğum tarihinizi giriniz")
gun = input("Gün (gg): ")
ay = input("Ay (aa): ")
yil = input("Yıl (yyyy): ")

while True:
    for i in range(10):
        time.sleep(.3)
        print(".",end="",flush=True)
    clear()
    sifre = input("\n4 haneli bir şifre giriniz: ")
    if len(sifre) == 4:
        if sifre.startswith("0"):
            print("Şifreniz 4 haneli olmak zorunda olduğu için ilk hanesi '0' olamaz!")
            continue
        elif int(sifre)-1234 == 0 or (int(sifre)-1234)%1111 == 0 or int(sifre)-8765 == 0 or (int(sifre)-8765)%1111 == 0:
            print("Birbiriniz takip eden rakamları şifrenizde kullanmayınız!")
            continue
        elif int(sifre)%1111 == 0:
            print("Şifreniz aynı rakamlardan oluşamaz!")
            continue
        elif sifre == (gun+ay) or sifre == (ay+yil) or sifre == (gun+yil) or sifre == (yil):
            print("Güvenlik açısından doğum tarihinizi şifre olarak kullanmayınız!")
            continue
    if len(sifre) != 4:
        print("Şifreniz 4 haneli olmak zorunda!")
        continue
    else:
        print("Giriş Başarılı!")
        break