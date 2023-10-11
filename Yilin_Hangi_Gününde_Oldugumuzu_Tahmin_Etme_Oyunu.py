import time

tahmin = int(input("Sence Yılın Kaçıncı Günündeyiz ?: "))

guncel_zaman = time.localtime()

if tahmin == guncel_zaman[7]:
	print("Helal Olsun Doğru Bildin !")

if tahmin > guncel_zaman[7]:
	yakinlik = int(tahmin - guncel_zaman[7])
	print("Yanlış Bildin !")
	time.sleep(1)
	print("Doğru Cevaba" , yakinlik , "Gün Yaklaştın !")
	time.sleep(1)
	print("Doğru Cevap:" , guncel_zaman[7])
	time.sleep(1)

if tahmin < guncel_zaman[7]:
	yakinlik = int(guncel_zaman[7] - tahmin)
	print("Yanlış Bildin !")
	time.sleep(1)
	print("Doğru Cevaba" , yakinlik , "Gün Yaklaştın !")
	time.sleep(1)
	print("Doğru Cevap:" , guncel_zaman[7])
	time.sleep(1)