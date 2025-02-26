liste = [1,2,3,4,5,6,7,8]
for i in liste:
    if(i % 2 ==0):
        print(i)


liste =  [1,2,3,4,5,6,7,8]
toplam = 0
for i in liste:
    toplam = toplam + i
    print(toplam)


liste =  [1,2,3,4,5,6,7,8]
toplam = 0
for sayı in liste:
    if(sayı % 2==0 ):
        print(sayı,sayı*sayı)





urunler = [
    {'name':'iphone 8', 'price': '4000' },
    {'name':'iphone 8 Plus', 'price': '5000' },
    {'name':'iphone X', 'price': '6000' },
    {'name':'iphone XR', 'price': '7000' },
    {'name':'iphone 11', 'price': '8000' },
    {'name':'samsung s10', 'price': '6000' },
]


# 1- Tüm ürün bilgilerini listeleyiniz.
# 2- Ürünlerin fiyatları toplamı nedir ?
# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.

#SOLVE
# 1- Tüm ürün bilgilerini listeleyiniz.
for urun in urunler:
    print(f"urun adı:{urun["name"]}  fiyatı:{urun["price"]} ")


# 2- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    toplam = toplam + int(urun["price"])
    print(f"toplam urun fiyatı:{toplam}")



# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz ?
for urun in urunler:
    if(int(urun["price"]) <= 6000):
        print(urun)


# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz.
kelime = input("ne aramıştınız:")
for urun in urunler:
    if (urun['name'].find(kelime.lower()) > -1):
        print(f"urunun adı:{urun["name"]} urunun fiyatı:{urun["price"]}")




#WHİLE

i = 1
while i<50:
    if(i % 2 == 0 ):
        print("çift sayıdır",i)
    else:
        print("tek sayıdır",i)
    i += 1




sayilar = [4,6,9,10,35,57,89,125,244]
# 1: sayilar listesini while ile ekrana yazdırın.
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

#SOLVE:
# 1: sayilar listesini while ile ekrana yazdırın.
i = 0
while (i< len(sayilar)):
    print(sayilar[i])
    i += 1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
başlangıç = int(input("başlangıç değerini gir"))
bitiş = int(input("bitiş değerini gir"))

i = başlangıç 
while (i < bitiş):
    i += 1
    if(i % 2 == 1):
        print(i)


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100
while (i>0):
    print(i)
    i -= 1



# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
sayılar = []
i = 0
while (i<5):
    sayı = int(input("bir sayı giriniz:"))
    sayılar.append(sayı)
    i += 1

sayılar.sort()
print(sayılar)





#    1Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    2** ürün sayısını kullanıcıya sorun.
#    3** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    4** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

#SOLVE
adet = int(input("kaç adet ürün eklemek istiyorsunuz"))
i = 0
urunler = []
while(i < adet):
    urunadı = input("urun adı giriniz:")
    fiyat = int(input("urun fiyatı giriniz"))
    urunler.append({
        "urunadı": urunadı,
        "urunfiyatı": fiyat
    })
    i += 1


for urun in urunler:
    print(f"urun adı:{urun["urunadı"]}  urun fiyatı:{urun["urunfiyatı"]}")


a = 0
while (a < len(urunler)):
    print(f"ürün adı: {urunler[a]['urunadı']} ürün fiyatı: {urunler[a]['urunfiyatı']}")
    a += 1




#RANGE(ÇARPIM TABLOSU VE ASAL SAYI)

# 1- Çarpım tablosu hazırlayınız.
# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..

#SOLVE
# 1- Çarpım tablosu hazırlayınız.
for i in range(1,11):
    print("******")
    for k in range(1,11):
        print("{}*{}= {}".format(i,k,i*k))


# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..
sayı = int(input("bir sayı gir:"))
asalmı = True

for i in range(2,sayı):
    if(sayı % i == 0):
        asalmı = False
        break
if asalmı:
    print("sayı asal sayıdır")
else:
    print("sayı asal sayı değildir")





#1-100 arasında rastgele üretilecekbir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak=5)
#**"random modülü" için "python random" şeklinde arama yapın
#**100 üzerinden puanlama yapın. Her soru 20 puan
#**Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın

import random
sayı = random.randint(1,100)
hak = 5 
sayac = 0

while(hak > 0):
    hak -=1
    sayac +=1
    tahmin = int(input("bir sayı seç:"))

    if(sayı == tahmin):
        print(f"tebrikler {sayac}. tahminde bildiniz.Toplam puanınız:{100-(20)*(sayac-1)}")
        break
    elif(sayı > tahmin):
        print("yukarı")
    else:
        print("aşşağı")
    
    if (hak == 0):
        print(f"hakkınız kalmadı.Tutulan sayı:{sayı}")





























