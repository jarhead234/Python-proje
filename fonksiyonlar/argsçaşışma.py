liste = [10,20,30,40,50]

def toplam(sayılar):
    sonuc = 0
    for i in sayılar:
        sonuc += i
    return sonuc

print(toplam(liste))



def toplam(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(10,20,30,40))
