num = (input('Введите элементы списка через запятую'))
numbers = num.split(',')
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)