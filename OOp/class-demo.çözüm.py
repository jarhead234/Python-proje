# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.


#SOLVE
# Comment isminde bir sınıf oluşturunuz.
class comment:
    def __init__(self,username,text,likes=0,dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = comment("sadıkturan","güzel kurs")
c2 = comment("ahmetyılmaz","güzel kurs")
c3 = comment("aliyılmaz","güzel kurs",50,100)
c4 = comment("salihyılmaz","güzel kurs")
c5 = comment("meriçyılmaz","güzel kurs",100)

comments = [c1,c2,c3,c4,c5]

for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")


