yaslar = [5,12,18,24,45]

def yetiskinmi(x):
    if (x<18):
        return False
    else:
        return True
    
sonuc = list(filter(yetiskinmi,yaslar))
print(sonuc)


sonuc = list(filter(lambda x: x%2==0,yaslar))
print(sonuc)



isimler = ["çınaar","yiğit","sena","ali","ahmet"]
sonuc = list(filter(lambda n: n[0]=="a", isimler))
print(sonuc)



sonuc = list(map(lambda n : n.upper(),filter(lambda n: n[0]=="a", isimler)))
print(sonuc)






users = [
    {"username":"sadikturan", "tweets": ["tweet 1","tweet 2"]},
    {"username":"cinarturan", "tweets": []},
    {"username":"senaturan", "tweets": ["tweet 1"]}
]

sonuc = list(map(lambda u: u["username"].upper(),filter(lambda u: len(u["tweets"])> 0,users)))
print(sonuc)