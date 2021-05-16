import re

check1 = True
check6 = True
check9 = True

#ЗАДАНИЕ 1
while check1:
    a = input('Введите код цвета или слово "Отмена": ')
    if a == "Отмена": break
    else:
        if len(a) == 7:
                s = re.compile('#[0-9A-Fa-f]{6}$')
                if s.match(a):
                        print('Корректное значение')
                else:
                    print('Не корректное значение')
        elif len(a) == 4:
                s = re.compile('#[0-9A-Fa-f]{3}$')
                if s.match(a):
                        print('Корректное значение')
                else:
                        print('Не корректное значение')
        else:
                print('Введите код цвета заново')
print('Задание 1 закончилось')

#ЗАДАНИЕ 6
while check6:
    b = input('Введите номер телефона или слово "Отмена": ')
    if b == "Отмена": break
    else:
        s1 = re.compile('^(\+7|8)\((909|912|922)\)\d{3}-\d{2}-\d{2}$')
        if s1.match(b):
            print('Корректное значение')
        else:
            print('Не корректное значение')
print('Задание 6 закончилось')

#ЗАДАНИЕ 9
while check9:
    c = input('Введите индекс или слово "Отмена": ')
    if c == "Отмена": break
    else:
        s2 = re.compile('^\d{6}$')
        if s2.match(c):
            print('Корректное значение')
        else:
            print('Не корректное значение')
print('Задание 9 закончилось')
