import os
import time

def clear():
    os.system('cls')

cevap = input("Admin Misin ?: ")

cevap2 = cevap.title()

while True:
    if cevap2 == "Evet":
        clear()

        print("\nAdmin Giriş Paneli \n---------------------------------")

        admin_usern = "dogan_admin"
        admin_passw = "dogan2008"

        admin_kullaniciadi = input("Kullanıcı Adınızı Giriniz: ")
        admin_sifre = input("Şifrenizi Giriniz: ")

        clear()

        if admin_usern == admin_kullaniciadi and admin_passw == admin_sifre:
            print("Kullanıcı Adı ve Şifreniz Doğru... \nGiriş Başarılı... \nHoş Geldin Admin !") 
            break

        elif admin_usern != admin_kullaniciadi and admin_passw == admin_sifre:
            print("Kullanıcı Adınız Hatalı Lütfen Tekrar Deneyiniz...")
            time.sleep(2)

        elif admin_usern == admin_kullaniciadi and admin_passw != admin_sifre:
            print("Şifreniz Hatalı Lütfen Tekrar Deneyiniz...")
            time.sleep(2)

        elif admin_usern != admin_kullaniciadi and admin_passw != admin_sifre:
            print("Kullanıcı Adı ve Şifreniz Hatalı Lütfen Tekrar Deneyiniz...")
            time.sleep(2)
            
    if cevap2 == "Hayır": 
        karakter = "çğıöşüÇĞÖŞÜ"

        clear()

        print("\nKullanıcı Kayıt Paneli \n---------------------------------")
    
        usern = input("Bir Kullanıcı Adı Giriniz: ")
        passw = input("Bir Şifre Giriniz: ")

        if set(usern) or set(passw) & set(karakter):
            clear()
            print("Kullanıcı Adınızda veya Şifrenizde Türkçe Karakter Var Lütfen Tekrar Deneyiniz...")
            time.sleep(2)
            continue

        else:
            pass

        clear()

        print("Lütfen Biraz Bekleyiniz...")

        time.sleep(2)
        clear()

        print("\nKullanıcı Giriş Paneli \n---------------------------------")

        kullaniciadi = input("Kullanıcı Adınızı Giriniz: ")
        sifre = input("Şifrenizi Giriniz: ")

        clear()

        if usern == kullaniciadi and passw == sifre:
            print("Kullanıcı Adı ve Şifreniz Doğru... \nGiriş Başarılı... \nHoş Geldin" , usern)
            break

        elif usern != kullaniciadi and passw == sifre:
            print("Kullanıcı Adınız Hatalı Lütfen Tekrar Deneyiniz...")
            time.sleep(2)

        elif usern == kullaniciadi and passw != sifre:
            print("Şifreniz Hatalı Lütfen Tekrar Deneyiniz...")
            time.sleep(2)

        elif usern != kullaniciadi and passw != sifre:
            print("Kullanıcı Adı ve Şifreniz Hatalı Lütfen Tekrar Deneyiniz...")
            time.sleep(2)