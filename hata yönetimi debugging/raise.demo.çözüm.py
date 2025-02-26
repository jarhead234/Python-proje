# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
# 2- Girilen parola içinde türkçe karakter hatası veriniz.

#SOLVE
# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
def faktöriyel(x):
    x = int(x)

    if(x<0):
        raise ValueError("negatif değer")
    
    sonuc = 1
    for i in range(1,x+1):
        sonuc *=i
        
    return sonuc
for i in [5,2,7,"a",9,4,"5a"]:
    try:
        x = faktöriyel(i)  
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)


# 2- Girilen parola içinde türkçe karakter hatası veriniz.
def parolakontrol(parola):
    turkce_karakterler = "şçğöıi"
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez")
        else:
            pass
    
    print("geçerli parola")

parola = input("parola: ")

try:
    parolakontrol(parola)
except TypeError as e:
    print(e)