class AgeError(Exception):
    pass



def idk(age):
    if age < 0:
        raise AgeError("Yosh noto'g'ri!")
    else:
        print(f'Sizning yoshingiz: {age}')


try:
    x = int(input("Yoshingizni kiriting: "))
    idk(x)
except AgeError as e:
    print(f"Xtolik: {e}")
    