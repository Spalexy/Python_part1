# coding: utf-8

_author_ = 'Alexander Pridacha'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.

print('\nЗадача-1\n')
n = int(input('Введите произвольное целое число: '))
k = str(n)

print('Самая большая цифра в числе - ', max(k))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

print('\nЗадача-2\n')
a = int(input('Введите переменную a: '))
b = int(input('Введите переменную b: '))

b = a + b 
a = b - a 
b = b - a

print('\nЗначения переменных поменяли местами')
print('a = ', a)
print('b = ', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print('\nЗадача-3\n')

print('Вычисляем корни квадратного уравнения ax2 + bx + c = 0')

a = float(input('Введите значение а: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))

D = b ** 2 - (4 * a * c)
print('Дискриминант равен: ', D)

if D < 0:
    print('Вещественных корней нет')
elif D == 0:
    x = -b / 2 * a
    print('Корень уравнения равен: ', x)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('x1 = ', x1)
    print('x2 = ', x2)