class Animal:
    
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    
    def make_sound(self):
        return f"{self.name} says {self.sound}!"


    def __str__(self):
        return self.make_sound()


class Bird(Animal):
    def __init__(self, bird, sound):
        self.bird  = bird
        self.sound = sound
    def make_sound(self):
        return f"{self.bird} says {self.sound}!"
          
    


t1 = Animal("Dog", "Woof")
    
t1.make_sound()
t2 = Animal("Cat", "Myav")
t2.make_sound()
print(t1)
print(t2)