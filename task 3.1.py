import random

a = int(input("a"))
b = int(input("b"))
c = list()
z = 0
y = 0
for x in range(20):
    x = random.randint(a,b)
    c.append(x)
    if x % 2 == 0:
        z = z + 1
    elif x % 2 != 0:
        y = y + 1
print(f"Четные:{z}, Нечетные:{y}")