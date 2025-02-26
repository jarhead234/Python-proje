sayilar = [1,5,16,35,57,72,75,10]
# 1- sayilar listesindeki her bir elemanı yazdırın.
# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
# 3- Sayilar listesinde sayıların toplamı kaçtır ?
# 4- Sayilar listesindeki çift sayıların karesini alınız.
# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)

#SOLVE
# 1- sayilar listesindeki her bir elemanı yazdırın.

for sayi in sayilar:
    print(sayi)

# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
for sayi in sayilar:
    if(sayi % 5 == 0 ):
        print(sayi)

# 3- Sayilar listesinde sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
print(toplam)    


# 4- Sayilar listesindeki çift sayıların karesini alınız.
for sayi in sayilar:
    if(sayi % 2 == 0):
        print(sayi,sayi*sayi)


# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']

for urun in urunler:
    print(urun[1])


# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)
for urun in urunler:
    print(urun.find('iphone'))







