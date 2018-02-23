"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class BingoCard:
    def __init__(self, type=''):
        self.type = type

    def make_bingo_card(self):
        num_set = []
        num_line = []
        while len(num_set) < 27:
            x = random.randrange(1, 90)
            if num_set.count(x) == 0 and num_line.count(x) == 0:
                num_line.append(x)

                if len(num_line) == 5:
                    num_line.sort()
                    while len(num_line) < 9:
                        num_line.insert(random.randrange(0, 9), ' ')
                    for each in num_line.copy():
                        num_set.append(each)
                    num_line.clear()
        return num_set

    def bingo_str_4_prn(self, bingo_card):
        bingo_str = ''
        if self.type == 'man':
            top_border_line = '=' * 15 + '   USER   ' + '=' * 15 + '\n'
            bottom_border_line = '=' * 40
        else:
            top_border_line = '*' * 15 + '   COMP   ' + '*' * 15 + '\n'
            bottom_border_line = '*' * 40
        bingo_str += top_border_line
        for i in range(0, 27):
            if bingo_card[i] != ' ' and bingo_card[i] != '--' and bingo_card[i] < 10:
                bingo_str += '\t' + ' ' + str(bingo_card[i])
            else:
                bingo_str += '\t' + str(bingo_card[i])
            if i != 0 and (i == 8 or i == 17 or i == 26):
                bingo_str += '\n'
        bingo_str += bottom_border_line
        return bingo_str


def card_check(list, x):
    if x in list:
        list[list.index(x)] = '--'


user = BingoCard('man')
comp = BingoCard('')
user_list = user.make_bingo_card()
comp_list = comp.make_bingo_card()
print(user.bingo_str_4_prn(user_list))
print(comp.bingo_str_4_prn(comp_list))

bochka_set = []
while len(bochka_set) < 90:
    x = random.randint(1, 91)
    if x not in bochka_set:
        bochka_set.append(x)

i = 0
while len(bochka_set) > 0:
    x = bochka_set.pop()
    result = (x in user_list)
    print('Ход №{}\nНовый бочонок: {} (осталось {}). Подсказка:{}'.format(i + 1, x, len(bochka_set),
                                                                                    result))
    choice = input('1 - зачеркнуть, 2 - продолжить:')
    if choice != '1' and choice != '2':
        bochka_set.append(x)
        continue

    card_check(comp_list, x)
    card_check(user_list, x)

    if result and choice == '1':
        print('>> ОК\n')
    elif result and choice == '2':
        print('>> Ошибка: число в карте\n')
        break
    elif not result and choice == '2':
        print('>>ОК\n')
    else:
        print('>> Ошибка: число НЕ в карте\n')
        # print('choice:{},user_list.count({}):{} vs x in user_list:{}'.format(choice, x, user_list.count(x),result))
        break

    print(user.bingo_str_4_prn(user_list))
    print(comp.bingo_str_4_prn(comp_list))

    i += 1
