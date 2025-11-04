class BankAccount:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Yangi balansingiz {self.balance}")

        else:
            print("Balansda yetarli mablag' yo'q!")

        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Balans yetarli emas!")
        elif amount <= 0:
            print("Iltimos musbat son kiriting!")
        else:
            self.balance -= amount
            print(f"Sizning yangi balansingiz {self.balance}")

        
    def __str__(self):
        return f"Owner: {self.owner}, Balans: {self.balance}"


t1 = BankAccount("Ali", 1000)
print(t1)

t1.deposit(500)
print(t1)

t1.withdraw(500)

print(t1)