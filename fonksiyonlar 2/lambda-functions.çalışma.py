sonuc = (lambda a: a**2)(3)
print(sonuc)




toplama = (lambda a,b: a+b)
sonuc = toplama(2,4)
print(sonuc)




def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)
multiply3 = myFunc(3)

sonuc = multiply2(10)
sonuc = multiply2(20)
sonuc = multiply3(10)


print(sonuc)