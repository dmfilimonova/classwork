a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
while a + b < c or a + c < b or b + c < a:
    if a + b < c or a + c < b or b + c < a:
        print("не существует")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("прямоугольный")
elif a**2 + b**2 != c**2 or a**2 + c**2 != b**2 or c**2 + b**2 != a**2:
    print("непрямоугольный")
