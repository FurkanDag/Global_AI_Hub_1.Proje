import pandas as pd


def not_hesapla(satir):

    satir = satir[:-1]
    liste = satir.split(":")
    ogrenci_ismi = liste[0]
    notlar = liste[1].split(",")

    vize1 = int(notlar[1])
    vize2= int(notlar[2])
    final = int(notlar[3])

    ortalama = vize1 * (30 / 100) +vize2 * (30 / 100) + final * (40 / 100)

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA ile geçti"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA ile geçti"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB ile geçti"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "CB ile geçti"
    elif ortalama >= 65 and ortalama <= 74:
        harf = "CC ile geçti"
    elif ortalama >= 58 and ortalama <= 64:
        harf = "DC ile geçti"
    elif ortalama >= 50 and ortalama <= 57:
        harf = "DD ile geçti"
    elif ortalama >= 38 and ortalama <= 49:
        harf = "FD ile kaldı"
    else:
        harf = "FF ile kaldı"

    return ogrenci_ismi + " - Matematik dersi harf notu " + ":" + harf + "\n"


def notlari_oku():
    with open("matematik_dersi_ogrenci_notları.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():


    isim = input("Öğrencinin İsmini Giriniz: ")
    soyad = input("Öğrencinin Soyismi Giriniz: ")
    ogrenci_no = input("Öğrencinin Numarasını Giriniz ""\n")


    vize1 = input("Öğrencinin 1.vize sınavını giriniz: ")
    vize2 = input("Öğrencinin 2.vize sınavını giriniz:")
    final = input("Öğrencinin final sınavını giriniz:")

    with open("matematik_dersi_ogrenci_notları.txt", "a", encoding="utf-8") as file:
        file.write(isim + " " + soyad + ":" + ogrenci_no + "," + vize1 + "," + vize2 + ","+ final + "\n")


def not_kaydet():
    with open("matematik_dersi_ogrenci_notları.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))

    with open("ogrencilerin_harf_notları.txt", "w", encoding="utf-8") as file2:

        for i in liste:
            file2.write(i)


def frame_olustur():
    with open("ogrencilerin_harf_notları.txt", "r", encoding="utf-8") as file:
        veri = pd.DataFrame(file)
        print(veri)


def excele_aktar():
    with open("ogrencilerin_harf_notları.txt", "r", encoding="utf-8") as file:
        data = pd.DataFrame(file)
        data.to_excel("ogrencilerin_harf_notları.xlsx")



while True:
    secim = input(
        "\n""***********Lütfen yapmak istediğiniz işlemi seçiniz***********\n""1-Bilgilerin Girişi\n2- Notları Göster\n3- Notları Kaydet\n4- Data Frame Şeklinde Göster\n5- Excele Aktar\n6- Çıkış \n\n")

    if int(secim) == 1:
        not_gir()

    elif int(secim) == 2:
        notlari_oku()
    elif int(secim) == 3:
        not_kaydet()
        print("NOTLAR KAYDEDİLDİ""\n")

    elif int(secim) == 4:
        frame_olustur()

    elif int(secim) == 5:
        excele_aktar()

    else:
        print("\n""SİSTEMDEN ÇIKIŞ YAPILDI.")
        break