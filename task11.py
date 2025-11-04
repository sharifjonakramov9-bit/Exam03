class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    
    def move(self):
        return f"{self.brand} is moving!"

    
    def __str__(self):
        return self.move()


t1 = Vehicle("kkk", "lhr")
print(t1)    

class Car(Vehicle):
    def move(self):
        return f"{self.brand} is driving"



t2 = Car("kkk", "lhr")
print(t2)    
