def selamlama():
    print("merhaba")

selamlama()
 


def selamla():
      for i in range(0,3):
           print("merhaba")
selamla()


def toplam():
     return 20+10
sonuc = toplam()
print(sonuc)


def yaşhesapla():
     import datetime
     return datetime.datetime.now().year
def emeklilikyaşı():
     yaş = int(input("yaşınız nedir:"))
     return (65-yaş)
sonuc = emeklilikyaşı()
print(f"emekli olmanıza kalan süre:{sonuc}")




def selamlama(isim):
     return "merhaba " + isim
sonuc=selamlama("Ali")
print(sonuc)




def yashesapla(doğumyılı):
     import datetime
     return 2024 - doğumyılı
yashesapla(2004)
     


def emekliliğekaçyılkaldı(doğumyılı,isim):
     yas = yashesapla(doğumyılı)
     kalansure = 65 - yas 
     if kalansure>0:
          print(f"emekliliğinize {kalansure} yıl kalmıştır")
     else:
          print(f"zaten emekli oldunuz")

emekliliğekaçyılkaldı(2004,"ali")






# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız
# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

#SOLVE
# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def yazdır(text,kaçkez):
     for i in range(kaçkez):
          print(text,kaçkez)
yazdır("naber ali",3)


# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def hesaplama(kısakenar,uzunkenar):
     alan = kısakenar*uzunkenar
     çevre = (kısakenar+uzunkenar)*2
     print(f"diktörtgenin alanı:{alan} dikdörtgenin çevresi:{çevre} dir")
sonuc=hesaplama(10,20)


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
          if(sayı>1):
               for i in range(2,sayı):
                    if(sayı % i == 0):
                         break
               else:
                    print(sayı)

asalsayılarıbul(2,40)



# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def tambölenbelirleme(sayı):
    tambölenler = []

    for i in range(2,sayı):
        if(sayı % i == 0):
            tambölenler.append(i)
    return tambölenler        

sonuc = tambölenbelirleme(100)
print(sonuc)

          
              
                


     
     
    







        
      

