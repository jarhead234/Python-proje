sonuc = all([True,True,False])
sonuc = all([True,True,True])
sonuc = any([True,False,False])

# And => True and True => True => All()
# Or  => True or False => True => Any()


sayılar = [1,3,6,8,9,10]
sonuc = all([bool(sayı) for sayı in sayılar])