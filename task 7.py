import re
a = input("Введите строку")
words = re.sub('[.,?;:"!]', '', a)
words = words.split (" ")
for x in words[1:]:
    longest = words[0]
    if len(x) > len(longest):
        longest = x
print(longest)
print(len(longest))
