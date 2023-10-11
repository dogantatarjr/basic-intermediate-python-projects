import datetime
import time
import os

def clear():
    os.system('cls')

cinsiyet = input("Cinsiyetinizi giriniz: ")
cinsiyet_title = cinsiyet.title()

time.sleep(0.5)
clear()

bugun = datetime.datetime.today()
gun = bugun.day
ay = bugun.month

if cinsiyet_title == "Kadın":

    cocuk_kadın = input("Çocuğun var mı ?: ")
    cocuk_kadın_title = cocuk_kadın.title()

    time.sleep(0.5)
    clear()

    if cocuk_kadın_title == "Yok":
        print("İnşallah bir gün olur :)")
    
    if cocuk_kadın_title == "Var":
        if gun == 9 and ay == 5:
            print("ANNELER GÜNÜN KUTLU OLSUN !!!")
        else:
            print("İnşallah çocuğun ile güzel günler geçirirsin :)")


if cinsiyet_title == "Erkek":

    cocuk_erkek = input("Çocuğun var mı ?: ")
    cocuk_erkek_title = cocuk_erkek.title()

    time.sleep(0.5)
    clear()

    if cocuk_erkek_title == "Yok":
        print("İnşallah bir gün olur :)")
    
    if cocuk_erkek_title == "Var":
        if gun == 20 and ay == 6:
            print("BABALAR GÜNÜN KUTLU OLSUN !!!")
        else:
            print("İnşallah çocuğun ile güzel günler geçirirsin :)")