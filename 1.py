"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

"""

HEX = 16
num: int = int(input('Input a number: '))
hex_structure = '0123456789abcdef'
hex_string = ''
print(hex(num))  # check

while num > 0:
    hex_string = hex_structure[num % HEX] + hex_string
    num = num // HEX

print(f'hex(num):{hex_string}')

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение * дробей. 
Для проверки своего кода используйте модуль fractions

"""
from fractions import Fraction

a = str(input('Input first fraction like a/b: '))
b = str(input('Input second fraction like a/b: '))


def numerator_denominator(x):
    num_x, den_x = map(int, x.split('/'))
    return num_x, den_x


def sum_fraction(x, y):
    num_x, den_x = numerator_denominator(x)
    num_y, den_y = numerator_denominator(y)
    num_z = num_x * den_y + num_y * den_x
    den_z = den_x * den_y
    return print(f'Amount {x} and {y}: {num_z}/{den_z}')


def com_sum_fraction(x, y):
    num_x, den_x = numerator_denominator(x)
    num_y, den_y = numerator_denominator(y)
    num_z = num_x * num_y
    den_z = den_x * den_y
    return print(f'Composition {x} and {y}: {num_z}/{den_z}')


sum_fraction(a, b)
com_sum_fraction(a, b)


# check

c = Fraction(a)
d = Fraction(b)

sum_ab = c + d
com_ab = c * d

print(sum_ab, com_ab)