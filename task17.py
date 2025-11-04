
class User:

    def __init__(self, username, email, is_active=bool):
        self.username = username
        self.email = email
        self.is_active = is_active


        
    def deactivate(self):
        self.is_active = False

    def activete(self):
        self.is_active = True

    
    def save(self):
        return f"Slom {self.username}! sizning emaillingiz -> {self.email} ({self.is_active})"

        with open("user.txt", "a") as f:
            f.write(f"Slom {self.username}! sizning emaillingiz -> {self.email} ({self.is_active})")

    
t1 = User("Ali", "@ali")
t1.deactivate()
print(t1.save())
t2 = User("Vali", "@vali")
t2.activete()
print(t2.save())

