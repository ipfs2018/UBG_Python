# Эти задачи необходимо решить используя регулярные выражения!
import re
# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка,
# ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
print('\nLvl:normal, ex#1')
name, surname, email = input('Введите имя, фамилию, email:').split()
print(name, surname, email)
pattern1 = '^[А-Я][а-я]+$'
pattern2 = '^[a-z_0-9]+@[a-z0-9]+\.(ru|org|com)$'
print('Имя ОК.' if re.match(pattern1, name) else 'С именем что-то не так.')
print('Фамилия ОК.' if re.match(pattern1, surname) else 'С фамилией что-то не так.')
print('Email ОК.' if re.match(pattern2, email) else 'С email что-то не так.')

# Задача - 2:
# Вам дан текст:
print('\nLvl:normal, ex#2')
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern3='\.\.'
print('\nЕсть несколько точек подряд.' if re.search(pattern3,some_str) else '\nНесколько точек подряд не найдено.')
# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!