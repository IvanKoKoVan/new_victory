col  = int(input('Введите количество элементов'))
result = []
for i in range(col):
    number = int(input('Введите число'))
    result.append(number)
result.sort()
print(result)