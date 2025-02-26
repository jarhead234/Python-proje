def usalma(taban,us):
    return taban ** us
sonuc = usalma(10,2)
print(sonuc)



def usalma(taban,us=2):
    return taban ** us
sonuc = usalma(10)
print(sonuc)




def toplama(a,b):
    return a + b

def çıkarma(a,b):
    return a - b

def işlem(a,b,Fm):
    return Fm(a,b)

sonuc = işlem(5,8,çıkarma)
print(sonuc)