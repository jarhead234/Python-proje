sayılar = [1,5,6,7,8,9]
isimler = ["ali","mehmet","buse","esra"]

sonuc = min(isimler)
sonuc1 = min([len(isim) for isim in isimler])
sonuc2 = min(isimler, key = lambda n: len(n))
print(sonuc2)




urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000}
]

sonuc = min(urunler, key = lambda urun:urun["price"])
sonuc1 = min(urunler, key=lambda urun: urun['price'])['title']
print(sonuc1)




max = 0
for urun in urunler:
    if urun["price"]>max:
        max = urun["price"]

print(max)