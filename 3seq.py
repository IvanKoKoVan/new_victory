#(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

#Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
#Затем он вводит элементы 2-го списка
#Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
#Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
#Введите элементы 2-го списка: 2,5
#Результат: 1,3,4
#Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
num = (input('Введите элементы 1-го списка через зяпятую'))
num_1 = num.split(',')
num = (input('Введите элементы 2-го списка через запятую'))
num_2 = num.split(',')
for i in num_1[:]:
    if i in num_2:
        num_1.remove(i)
print(num_1)