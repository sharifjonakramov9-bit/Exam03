print("Salom ismingiz va yoshingizni kiriting!")

x = input("Ism: ").strip()
y = input("Yosh: ").strip()
with open("data.txt", "a") as f:
    f.write(f"`{x} - {y} yosh`\n")
