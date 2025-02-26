i = 1

while i <= 100:
    if(i%2 == 1):
        print("tek sayı:", i)
    else:
        print("çift sayı:", i)
    i += 1


username = ''
while not username:
    username = input("kullanıcı adınız:")
print("girdiğiniz kullanıcı adınız:", username)