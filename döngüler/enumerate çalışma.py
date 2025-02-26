markalar = ["bmw","mercedes","opel"]

obj = enumerate(markalar)
print(list(obj))


for index,value in enumerate(markalar,1):
    print(index,value)


liste1 = ["a","b","c","d"]
liste2 = [1,2,3,4,5]
liste3 = [100,200,300,400,500]

print(list(zip(liste1,liste2,liste3)))

for item in zip(liste1,liste2,liste3):
    print(item)


for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)