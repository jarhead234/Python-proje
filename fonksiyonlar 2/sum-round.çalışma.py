sayılar = [1,2,5,7,8]
sonuc = sum(sayılar)
sonuc1 = sum(sayılar,10)
print(sonuc1)



urunler = [
    {"title":"iphone x", "price": 5000},
    {"title":"iphone xr", "price": 6000},
    {"title":"iphone 11", "price": 7000},
    {"title":"iphone 11 Pro", "price": 0},
]

toplamFiyat = sum(urun["price"] for urun in urunler)
urunAdeti = len([urun for urun in urunler if urun["price"]>0])
sonuc = toplamFiyat / urunAdeti
print(sonuc)


sonuc = round(10.2)
sonuc = round(10.6)
sonuc = round(10.5)
sonuc = round(1.424242, 2)
sonuc = round(1.426242, 2)
sonuc = round(1.426242, 4)

print(sonuc)

