import time
import os

def clear():
	os.system('cls')

print("""
--------------------
 Turnuva Oluşturucu
--------------------""")
takim_sayisi = int(input("Turnuvada Kaç Takım Olmasını İstersiniz ?: "))
takim_sayisi2 = int(takim_sayisi + 1)

takimlar = []

time.sleep(0.3)
clear()

for i in range(1,takim_sayisi2):
	print("Takım" , str(i) + ":")
	print("-" * 20)
	takim = input("")
	print("""
	""")
	takimlar.append(takim)

clear()

takim_sayisi3 = (takim_sayisi - 1)

for a in takimlar:
	print(takimlar[0] , "-" , takimlar[takim_sayisi3])
	takim_sayisi3 = int(takim_sayisi3 - 1)