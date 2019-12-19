import random

a = int(input("a"))
b = int(input("b"))
c = list()
for x in range(20):
    x = random.randint(a,b)
    c.append(x)
print(c)