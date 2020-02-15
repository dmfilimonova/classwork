str = input("введите строку")
vowel = ["а","е","ё","и","о","у","ы","э","ю","я"]
words = str.split(" ")
summ = 0
for x in words:
    if x[0] in vowel:
        summ = summ + 1
print(summ)



