import random

result = random.random()
result = random.random() * 100
result = int(random.uniform(1,100))
result = random.randint(1,100)

print(result)


names = ["ali","yağmur","ismail","kübra"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
print(result)



liste = list(range(10))
random.shuffle(liste)
print(liste)



liste = range(100)
result = random.sample(liste,3)
print(result)