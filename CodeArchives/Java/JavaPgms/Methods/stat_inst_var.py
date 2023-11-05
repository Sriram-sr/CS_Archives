from re import L


class Fruits:
    count = 0
    def __init__(self,fruit,count):
        self.fruit=fruit
        self.count=count
        Fruits.count = Fruits.count + count


print(Fruits.count)
instance=Fruits('apple',3)
print(Fruits.count)        
print(type(instance).count)
print(instance.__class__.count)