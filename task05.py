import json

fayl = "data.json"

try:
    with open(fayl, "r") as f:
        x = json.load(f)
except:
    print("Fayl topilmadi!")
    exit()

for i in x:
    print(f"Name: {i['name']}, Age: {i['age']}")