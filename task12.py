class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def move(self):
        return f"{self.name} ismi, {self.age} yoshi"

    
    def __str__(self):
        return self.move()


t1 = Person("kkk", 18)
print(t1.move())    

class Student(Person):
    def move(self, grade):
        return f"{self.name} nomli o'quvchi, yoshi {self.age}da, klass {grade}"



t2 = Student("kkk", 19)
print(t2.move("A"))    
