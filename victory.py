months = {
    '01': 'январь',
    '02': 'февраль',
    '03': 'март',
    '04': 'апрель',
    '05': 'май'
}

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое'
}

again = 'да'
while again.lower() == 'да':
    right: int = 0
    wrong: int = 0

    query1 = input('Год рождения Ломоносова М.С.') #1711
    if query1 =='01.01.1711':
        print("Верно")
        right += 1
    else:
        data = '01.01.1711'
        day, month, year = data.split('.')
        print(days[day], months[month], year, 'года')
        wrong += 1

    query2 = input('Год рождения Иссака Ньютона')  # 1643
    if query2 == '02.02.1643':
        print("Верно")
        right += 1
    else:
        data_1 = '02.02.1643'
        day, month, year = data_1.split('.')
        print(days[day], months[month], year, 'года')
        wrong += 1

    query3 = input('Год рождения Кулибина И.П.')  # 1735
    if query3 == '03.03.1735':
        print("Верно")
        right += 1
    else:
        data_2 = '03.03.1735'
        day, month, year = data_2.split('.')
        print(days[day], months[month], year, 'года')
        wrong += 1

    query4 = input('Год рождения Стива Джобса')  # 1955
    if query4 == '04.04.1955':
        print("Верно")
        right += 1
    else:
        data_3 = '04.04.1955'
        day, month, year = data_3.split('.')
        print(days[day], months[month], year, 'года')
        wrong += 1

    query5 = input('Год рождения Николы Теслы')  # 1856
    if query5 == '05.05.1856':
        print("Верно")
        right += 1
    else:
        data_4 = '05.05.1856'
        day, month, year = data_4.split('.')
        print(days[day], months[month], year, 'года')
        wrong += 1

    print('Верно', right)
    print('Ошибок', wrong)
    print('Верно', right * 100 / 5, 'percent')
    print('Ошибок', wrong * 100 / 5, 'percent')

    again = input('Начнем игру сначала?')