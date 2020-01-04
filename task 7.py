a = input("Введите строку")
words = a.split(" ")
longest = words[0]
for x in words[1:]:
    if len(x) > len(longest):
        longest = x
print(longest)
print(len(longest))
