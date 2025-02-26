# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız
# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.


#solve
# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def yazdır(txt,adet):
    for i in range(adet):
        print(txt,adet)
    
yazdır("Naber ali",5)


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def hesapla(kisa, uzun):
     alan = kisa * uzun
     cevre = 2 * (kisa + uzun)

     return f"alan: {alan} çevre: {cevre}"

 #print(hesapla(5,7))



# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
def yazıtura():
    import random
    sayı = random.random()

    if sayı>0.5:
        return "tura"
    else:
        return "yazı"
    
print(yazıtura())



# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız
def asalsayılarıbul(sayı1,sayı2):
    for sayı in range(sayı1,sayı2+1):
        if (sayı>1):
            for i in range(2,sayı):
                if sayı % i == 0:
                    break
            else:
                print(sayı)

asalsayılarıbul(10,100)



# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def tambölenbelirleme(sayı):
    tambölenler = []

    for i in range(2,sayı):
        if(sayı % i == 0):
            tambölenler.append(i)
    return tambölenler        

sonuc = tambölenbelirleme(100)
print(sonuc)










        
