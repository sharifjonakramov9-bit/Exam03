class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    
    def divide(self):
        try:
                return self.a / self.b
        except ZeroDivisionError:
            print("Bo'lishda xatolik")

    def __str__(self):
        return f"Calculator {self.a}, {self.b}"
    

t1 = Calculator(3, 5)
t1.divide()
print(t1)
