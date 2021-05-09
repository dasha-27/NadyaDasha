import re

#ЗАДАНИЕ 1
a = input('Введите код цвета: ')
if len(a) == 7:
        s = re.compile('#[0-9A-F]{6}$')
        if s.match(a):
                print('Корректное значение')
        else:
                print('Не корректное значение')
elif len(a) == 4:
        s = re.compile('#[0-9A-F]{3}$')
        if s.match(a):
                print('Корректное значение')
        else:
                print('Не корректное значение')
else:
        print('Введите код цвета заново')

#ЗАДАНИЕ 6
b = input('Введите номер телефона: ')
s1 = re.compile('^(\+7|8)\((909|912|922)\)\d{3}-\d{2}-\d{2}$')
if s1.match(b):
    print('Корректное значение')
else:
    print('Не корректное значение')

#ЗАДАНИЕ 9
c = input('Введите индекс: ')
s2 = re.compile('^\d{6}$')
if s2.match(c):
    print('Корректное значение')
else:
    print('Не корректное значение')