def my_print(name, age, city):
    """
    Задание - 1
    Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
    Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
    """
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


name, age, city = input('\nEasy, task#1\nВведите через пробел имя, возраст, город:').split()
print(my_print(name, age, city))


def my_max(a, b, c):
    """
    Задание - 2
    Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
    """
    return max(a, b, c)


a, b, c = input('\nEasy, task#2\nВведите через пробел 3 числа:').split()
print(my_max(a, b, c))


def max_strs(list):
    """
    Задание - 3
    Создайте функцию, принимающую неограниченное количество строковых аргументов,
    верните самую длинную строку из полученных аргументов

    """
    results = map(lambda item: len(item), list1)
    max_len_str = max(results)
    results = filter(lambda item: len(item) == max_len_str, list1)
    return results


list1 = input('\nEasy, task#3\nВведите через пробел произвольные значения:').split()
print(list(max_strs(list1)))
