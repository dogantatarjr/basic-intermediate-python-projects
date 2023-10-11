import sqlite3

veritabani = sqlite3.connect("kutuphane.db")
veritabani.row_factory=sqlite3.Row
imlec = veritabani.cursor()

sorgulama = input("""
Kitap adından sorgulamak için: K
Yazar adından sorgulamak için: Y
Basım yılından sorgulamak için: B

>""").title()

if sorgulama == "K":    
    kitap_adi = input("Kitap Adı:")
    imlec.execute("SELECT * FROM Kitap WHERE KitapAdi LIKE ('{}' || '%')".format(kitap_adi))
if sorgulama == "Y":    
    yazar_adi = input("Yazar Adı:")
    imlec.execute("SELECT * FROM Kitap WHERE YazarAdi LIKE ('{}' || '%')".format(yazar_adi))
if sorgulama == "B":    
    basim_yili = input("Basım Yılı:")
    imlec.execute("SELECT * FROM Kitap WHERE BasimYili LIKE ('{}' || '%')".format(basim_yili))

veriler = imlec.fetchall()

for veri in veriler:
    print("Kitap Adı:",veri["KitapAdi"],"\nYazar Adı:",veri["YazarAdi"],"\nBasım Yılı:",veri["BasimYili"],"\n")