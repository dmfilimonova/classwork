import re
n = int(input("Введите число"))
str = input("Введите строку из слов")
summ = 0
words = re.sub(r'[,.?";:]', '', str)
words = words.split(" ")
for x in words[0:]:
    if len(x) == n:
        summ = summ + 1
print(f"Количество слов, длина которых равнa n:{summ}")


