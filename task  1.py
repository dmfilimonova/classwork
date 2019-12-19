a = int(input("Введите a"))
b = int(input("Введите b"))
c = int(input("Введите c"))
if a > b and a > c:
    print(f"Наибольшее:{a}")
elif b > a and b > c:
    print(f"Наибольшее:{b}")
else:
    print(f"Наибольшее:{c}")


