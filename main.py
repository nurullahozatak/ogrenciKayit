def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    not1 = input("1.Not: ")
    not2 = input("2.Not: ")
    not3 = input("3.Not: ")

    with open("sinav_notlari.txt", "a", encoding= "utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')


def not_kaydet():
    with open("sinav_notlari.txt", "r", encoding= "utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)

def ortalamaları_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(satir, end="")

def sonuc_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir), end="")


def not_hesapla(satir):
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama >= 90 and ortalama<=100:
        harf = 'AA'
    elif ortalama>= 85 and ortalama <= 89:
        harf = 'BA'
    elif ortalama >= 80 and ortalama <= 84:
        harf = 'BB'
    elif ortalama>= 75 and ortalama <= 79:
        harf = 'CB'
    elif ortalama >= 70 and ortalama <= 74:
        harf = 'CC'
    elif ortalama>= 65 and ortalama <= 69:
        harf = 'DC'
    elif ortalama >= 60 and ortalama <= 64:
        harf = 'DD'
    elif ortalama>= 55 and ortalama <= 59:
        harf = 'FD'
    else :
        harf = 'FF'

    return ogrenciAdi + ": "+ harf + "\n"


while True:
    islemSec = input("1- Not Gir\n2- Notları Kaydet\n3- Notları Göster\n4- Sonucları Göster \n5- Çıkış \n")

    if islemSec == "1":
        not_gir()
    elif islemSec == "2":
        not_kaydet()
    elif islemSec == "3":
        ortalamaları_oku()
    elif islemSec == "4":
        sonuc_oku()
    else:
        break