import random

liste = ["köpek","kedi","orangutan","gergedan","aslan","iguana","balık","zürafa","armadilo","tavşan"]
kelime = random.choice(liste)
kelime_len = len(kelime)
print(kelime)
print("_"*kelime_len)

while True:
    for h in kelime:
        harf = str(input("Harf giriniz: "))
        if h == harf:
            sira = kelime.index(harf)+1
            print("_"*(sira-1)+harf+"_"*(kelime_len-sira))