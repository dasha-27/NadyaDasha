# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:51:33 2021

@author: Дарья
"""

#ЗАДАНИЕ 3
def shift(a, k):
    return a[-k:]+a[:-k]

nums = [6, 5, 6, 3, 1, 9, 0]
print(nums)
shift(nums, -2)
print(nums)
shift(nums, 3)
print(nums)



#ЗАДАНИЕ 8
def number_to_words(n):
    hund = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот',
            6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
    dec = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
           6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
    one = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

    n1 = str(n)
    if len(n1) == 1:
        return one[int(n1[0])]
    if len(n1) == 2:
        return '%s %s' % (dec[int(n1[0])], one[int(n1[1])])
    else:
        return '%s %s %s' % (hund[int(n1[0])], dec[int(n1[1])], one[int(n1[2])])

print(number_to_words(3))
print(number_to_words(20))
print(number_to_words(61))
print(number_to_words(201))
print(number_to_words(600))
print(number_to_words(810))
print(number_to_words(121))



#ЗАДАНИЕ 10
import random
def massiv(array):
    print("Исходный массив:")
    print(array)
    print("Минимальное и максимальное значения: ")
    minimax = [min(array), max(array)]
    return minimax

N = [random.randrange(9) for _ in range(10)]
print(massiv(N))