try:
    x = int(input("bir sayı girin: "))
    y = int(input("bir sayı girin: "))
    print(x+y)
except:
    print("bir hata oluştu.")




while True:
    try:
         x = int(input("bir sayı girin"))
         y = int(input("bir sayı girin"))
    print(x/y)
    except ZeroDivisionError as e:
    print("y sıfır olamaz")
    print(e)
    except ValueError as e:
    print("x ve y sayısal bir değer olmalıdır")
    print(e)
    else:
    print("herşey yolunda. ")
