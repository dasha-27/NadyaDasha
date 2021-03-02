# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:51:33 2021

@author: Дарья
"""
#комментарии:ctrl + 1

#ЗАДАНИЕ 3
# def shift(lst, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps):
#             lst.insert(0, lst.pop())


# nums = [4, 5, 6, 7, 8, 9, 0]
# print(nums)

# shift(nums, -2)
# print(nums)

# shift(nums, 3)
# print(nums)



#ЗАДАНИЕ 8
# def number_to_words(n):
#     hund = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 
#             6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
#     dec = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 
#            6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
#     one = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 
#            7: 'семь', 8: 'восемь', 9: 'девять'}
    
#     n1 = int(str(n)[0])
#     if (n < 10):
#         return one[n1]
    
#     n2 = int(str(n)[1])
#     if (n < 100):
#         return '%s %s' % (dec[n1], one[n2])
    
#     n3 = int(str(n)[2])
#     return '%s %s %s' % (hund[n1], dec[n2], one[n3])
    
# print(number_to_words(3))
# print(number_to_words(20))
# print(number_to_words(61))
# print(number_to_words(201))
# print(number_to_words(600))
# print(number_to_words(810))
# print(number_to_words(121))



#ЗАДАНИЕ 10
import numpy as np
import random
array = np.random.randint(0, 10, 5)
print("Исходный массив:")
print(array)
min = min(array)
max = max(array)
print("Минимальное и максимальное значения: ")
minimax = [min, max]
print(minimax)