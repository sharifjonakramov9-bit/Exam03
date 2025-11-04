
try: 
    with open("data.txt") as f:
        for i in f:
            i = i.strip()
        print(i)
        
except:
    print("Fayl topilmadi!")
