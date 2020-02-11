a = int(input("Введите год:"))
if a % 400 == 0 and a % 4 == 0:
    print("Високосный")
elif a % 100 == 0 and a % 400 != 0:
    print("Невисокосный")
else:
    print("Невисокосный")