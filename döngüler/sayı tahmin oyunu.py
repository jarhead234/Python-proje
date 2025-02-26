#1-100 arasında rastgele üretilecekbir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak=5)
#**"random modülü" için "python random" şeklinde arama yapın
#**100 üzerinden puanlama yapın. Her soru 20 puan
#**Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın

import random
sayı = random.randint(1,100)
hak = 5
sayaç = 0

while (hak > 0):
    hak -= 1
    sayaç += 1
    tahmin = int(input("bir tahminde bulunuz"))

    if sayı == tahmin:
        print(f"tebrikler {sayaç}. tahminde bildiniz. Toplam puanınız {100 - (20)*(sayaç-1)}")
        break
    elif (sayı > tahmin):
        print("yukarı")
    else:
        print("aşağı")

    if (hak == 0):
        print(f"hakkınız kalmadı.Tutulan sayı:{sayı}")
        
       
