import json

fayl = "data.json"


name = input("Name: ").strip()
age = input("Age: ").strip()

try:
    with open(fayl, "r") as f:
        x = json.load(f)
except:
    x = []

x.append({"name": name, "age": int(age)})

with open(fayl, "w") as f:
    json.dump(x, f, indent=4)
