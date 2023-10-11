kilo = float(input("Kilonuzu Giriniz (kg): "))
boy = float(input("Boyunuzu Giriniz (m): "))

vke = float(kilo / (boy * boy))

print("Vücut Kitle Endeksiniz: " , vke)
print("Vücut Kitle Endeksine Göre Durumunuz: ")

if vke < 18.5:
    print("Zayıf")
elif vke < 24.9:
    print("Normal Kilolu")
elif vke < 30:
    print("Fazla Kilolu")
elif vke < 35:
    print("Tip 1 Obez") 
elif vke < 40:
    print("Tip 2 Obez")
elif vke > 40:
    print("Morbid Obez")
elif vke > 50:
    print("Süper Obez")
elif vke > 60:
    print("Süper Süper Obez")