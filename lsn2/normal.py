import math
import random
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print('\nNormal, task #1')

list1 = [2, -5, 8, 9, -25, 25, 4]
list2 = []

for item1 in list1:
    if item1 > 0:
        sqrt_item1 = math.sqrt(item1)
        if sqrt_item1 == math.trunc(sqrt_item1):
            list2.append(int(sqrt_item1))

print('result:', list2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('\nNormal, task #2')

list3 = '12.09.2013'.split('.')

day = int(list3[0])
month = int(list3[1])

if 0 < day < 31:
    if   day == 1: day = 'первое'
    elif day == 2: day = 'второе'
    elif day == 3: day = 'третье'
    elif day == 4: day = 'четвертое'
    elif day == 5: day = 'пятое'
    elif day == 6: day = 'шестое'
    elif day == 7: day = 'седьмое'
    elif day == 8: day = 'восьмое'
    elif day == 9: day = 'девятое'
    elif day == 10: day = 'десятое'
    elif day == 11: day = 'одиннадцатое'
    elif day == 12: day = 'двенадцатое'
    elif day == 13: day = 'тринадцатое'
    elif day == 14: day = 'четырнадцатое'
    elif day == 15: day = 'пятнадцатое'
    elif day == 16: day = 'шестнадцатое'
    elif day == 17: day = 'семнадцатое'
    elif day == 18: day = 'восемнадцатое'
    elif day == 19: day = 'девятнадцатое'
    elif day == 20: day = 'двадцатое'
    elif day == 21: day = 'двадцать первое'
    elif day == 22: day = 'двадцать второе'
    elif day == 23: day = 'двадцать третье'
    elif day == 24: day = 'двадцать четвертое'
    elif day == 25: day = 'двадцать пятое'
    elif day == 26: day = 'двадцать шестое'
    elif day == 27: day = 'двадцать седьмое'
    elif day == 28: day = 'двадцать восьмое'
    elif day == 29: day = 'двадцать девятое'
    elif day == 30: day = 'тридцатое'
    elif day == 31: day = 'тридцать первое'
else:
    print('Дата задана некорректно:'+list3[0]+'.')

if 0 < month < 12:
    if   month == 1: month = 'января'
    elif month == 2: month = 'февраля'
    elif month == 3: month = 'марта'
    elif month == 4: month = 'апреля'
    elif month == 5: month = 'мая'
    elif month == 6: month = 'июня'
    elif month == 7: month = 'июля'
    elif month == 8: month = 'августа'
    elif month == 9: month = 'сентября'
    elif month == 10: month = 'октября'
    elif month == 11: month = 'ноября'
    elif month == 12: month = 'декабря'
else:
    print('Месяц задан некорректно:'+list3[0]+'.')


print(day + ' ' + month + ' ' + list3[2] + ' года')


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print('\nNormal, task #3')

n=random.randint(1,10)
list4=[]
i=0
while i<n:
    list4.append(random.randint(-100,100))
    i+=1
print('n='+str(n))
print(list4)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print('\nNormal, task #3')
list5 = [1, 2, 4, 5, 6, 2, 5, 2]
list_a = set(list5)
list_b=[]

for item in list5:
    if list5.count(item)==1: list_b.append(item)

print(list_a, list_b)