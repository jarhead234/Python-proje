sayılar = [1,2,3,4,5,6]
kareleri = []
for sayı in sayılar:
    kareleri.append(sayı**2)

print(kareleri)



def kareAl(sayı):
    return sayı**2
sonuc = list(map(kareAl,sayılar))
print(sonuc)



sonuc = list(map(lambda sayı:sayı**2,sayılar))
print(sonuc)