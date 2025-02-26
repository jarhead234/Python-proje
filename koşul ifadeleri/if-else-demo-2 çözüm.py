# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.

benzinFiyat = 46.72
dizelFiyat = 47.95
ortalamaYakitTuketimi = float(input("100 km deki ortalama yakıtTuketimi"))
gidilecekYol = float(input("gidilecek yok kaç km"))
yakitTipi = input("yakıt tipiniz nedir")

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitÜcreti = benzinFiyat * toplamYakitTuketimi
elif(yakitTipi == "dizel"):
    toplamYakitÜcreti = benzinFiyat * toplamYakitTuketimi
else:
    print("yanlış yakıt tipi girdiniz")


print(toplamYakitÜcreti)