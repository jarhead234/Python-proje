class product:
    def __init__(self,name,price,isActive=False):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product nesnesi oluşturuldu")

p1 = product("samsung s10",5000)
p2 = product("Iphone 12",8000,True)

print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)
        