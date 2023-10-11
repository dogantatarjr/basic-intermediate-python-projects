def faktoriyel(sayi):
    fakt = 1
    for i in range(1,sayi+1):
        fakt = fakt * i
    return fakt

def permutasyon(n,r):
    perm = faktoriyel(n) / faktoriyel(n-r)
    return perm

def kombinasyon(n,r):
    komb = faktoriyel(n) / (faktoriyel(n-r) * faktoriyel(r))
    return komb

n = int(input("'n' değerini giriniz: "))
r = int(input("'r' değerini giriniz: "))

p = permutasyon(n,r)
c = kombinasyon(n,r)

print("P(" + str(n) + "," + str(r) + ") = " + str(int(p)))
print("C(" + str(n) + "," + str(r) + ") = " + str(int(c)))