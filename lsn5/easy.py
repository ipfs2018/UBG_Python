import os, sys


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def my_copy():
    file_name = os.path.basename(sys.argv[0])
    os.system('cp -f {} {}.copy'.format(file_name, file_name))


def my_dir_list(dir):
    return os.listdir(dir)


def my_mk_rm_dir(user_input):
    try:
        if user_input == '0':
            os.rmdir('dir_' + str(i))
        else:
            os.mkdir('dir_' + str(i))
    except FileExistsError:
        print('Директория ' + 'dir_' + str(i) + ' существует.')
    except FileNotFoundError:
        print('Директория ' + 'dir_' + str(i) + ' НЕ существует.')

if __name__ == '__main__':
    print('\nLvl: easy, ex#1')

    user_input = input('\nЛюбой ввод - создать, 0 - удалить 9-ть директорий, 1 - вывести содержимое текущей директории:')
    i = 1
    if user_input == '1':
        print(my_dir_list())
    else:
        for i in range(10):
            my_mk_rm_dir(user_input)

    my_copy()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
