class Rectangle:

    def __init__(self, width, height):
        self.width  = width
        self.height = height

    
    def area(self):
        return int(self.width) * int(self.height)

    
t1 = Rectangle(8, 9)
t2 = Rectangle(5, 7)
print(t1)
print(t2)
