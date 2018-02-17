import os, sys
import easy as lib

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
while True:
    print(
        '\n1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\nq. завершить программу\n')
    user_input = input('>')
    if user_input == '1':
        get_dir = input('введите имя папки:')
        try:
            os.chdir(get_dir)
        except FileNotFoundError:
            print('Папки с таким именем нет.')

        print('текущая папка:{}'.format(os.getcwd()))
    elif user_input == '2':
        print(lib.my_dir_list(os.getcwd()))
    elif user_input == '3':
        get_dir = input('введите имя папки:')
        os.system('rm -R {}'.format(get_dir))
        print('текущая папка:{}'.format(os.getcwd()))
        print(lib.my_dir_list('.'))
    elif user_input == '4':
        get_dir = input('введите имя папки:')
        try:
            os.mkdir(get_dir)
        except FileExistsError:
            print('Директория ' + 'dir_' + str(i) + ' существует.')
        except FileNotFoundError:
            print('Директория ' + 'dir_' + str(i) + ' НЕ существует.')

    elif user_input == 'q':
        break
    else:
        print('Некорректный ввод.')
