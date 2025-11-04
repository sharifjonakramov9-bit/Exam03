
try: 
    with open("data.txt", "r") as f:
        x = f.readlines()
        y = len(x)
        print(f"data.txt faylida {y} ta foydalanuvchi mavjud")
        
except:
    print("Fayl topilmadi!")
