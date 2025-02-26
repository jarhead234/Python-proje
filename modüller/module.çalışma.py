import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.ogrenci["ad"]
sonuc = module.topla(2,7)
print(sonuc)


import module as m
sonuc = m.sayi
sonuc = m.sayilar
print(sonuc)



from module import ogrenci, topla
sonuc = ogrenci
sonuc = topla(10,20)



from module import *
sonuc = sayi
sonuc = ogrenci["notlar"]
print(sonuc)



