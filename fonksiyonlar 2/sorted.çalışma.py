sayılar  = [1,22,44,5,33,25]
sonuc = sorted(sayılar)
print(sonuc)




users = [
    {"username":"Ali Erdoğan","tweets":["tweet 1","tweet 2"],"email":"info@gmail.com"},
    {"username":"cinarturan", "tweets":[]},
    {"username":"senaturan", "tweets":["tweet 1"],"name":"","phone":"434312134"}
]

sonuc = sorted(users,key=len)
sonuc1 = sorted(users,key=len, reverse=True)
sonuc2 = sorted(users, key = lambda user: user["username"])
sonuc3 = sorted(users, key = lambda user: len(user["tweets"]))
print(sonuc3)






kurslar = [
    {"title":"python kursu","students":25000},
    {"title":"web geliştirme kursu","students":35000},
    {"title":"javascript kursu","students":5000}
]

sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])
sonuc1 = sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True)
sonuc2 = map(lambda kurs: kurs["title"], sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True))
print(list(sonuc2))