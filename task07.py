class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def info(self):
        return f"{self.title} nomli kitob, {self.author} tomonidan yozilgan, ({self.year})"

    
    def __str__(self):
        return self.info()


t1 = Book("Nimadur", "Kimdur", 2025)
t1.info()
print(t1)
