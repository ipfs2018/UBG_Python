# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
print('\nHard, task #1')
equation = 'y = -12x + 11111140.2121'
x = 2.5
s_k = 1

k = int(equation[5:7])
b = float(equation[-13:])

if equation[4] == '-': s_k = -1

y=s_k*k*x+b

print('result:'+str(y))



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print('\nHard, task #2')
while True:
    user_date = input('Введите дату (dd.mm.yyyy):')

    day = int(user_date[0:2])
    month = int(user_date[3:5])
    year = int(user_date[-4:])

    if len(user_date) != 10:
        print('Неверный формат ввода данных: количество знаков.')
        continue
    elif 31 < day or day < 0:
        print('Неверный формат ввода данных: несуществующая дата.')
        continue
    elif 12 < month or month < 0:
        print('Неверный формат ввода данных: несуществующий месяц.')
        continue
    elif year < 0:
        print('Неверный формат ввода данных: несуществующий год.')
        continue
    else:
        print('Дата введена корректно:', day, month, year)
        break





# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3