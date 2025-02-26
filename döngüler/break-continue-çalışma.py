isim = "Ali Erdoğan"

for i in isim:
    if(i == "E"):
        continue
    print(i)


for i in isim:
    if(i == "E"):
        break
    print(i)


# 1-100 arasındaki çift sayılar toplamı.
i = 0
toplam = 0
while (i<=100):
    i += 1
    if (i % 2 == 1):
        continue
    toplam += i
print(f"toplam: {toplam}")