'''Подсчитать, сколько было выделено памяти под переменные'''

import sys
import ctypes
import struct
import platform


print(sys.version)
print(platform.architecture())
# Python 3.8.0
# '64bit'
print('*' * 50)

a = '123456789'


def revers_1(n):
    '''Поворот числа через арифметические действия'''

    n = int(n)
    rev = ''
    while True:
        rev += str(n % 10)
        n //= 10
        if n == 0:
            break
    return rev


def revers_2(n):
    'Поворот числа через создание новой строки и заполнения последней по 1 элементу'

    res = ''
    for i in n[::-1]:
        res += i
    return res


def revers_3(n):
    '''Поворот числа-строки через встоенный алгоритм'''

    return n[::-1]


'''Длительность работы от 1-й к 3-й функции снижалась, теперь проанализируем
количество затрачиваемой памяти на создание переменных'''


class ShowSize():

    def __init__(self):
        self._sum_mem = 0

    def _add(self, obj):
        spam = sys.getsizeof(obj)
        self._sum_mem += spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for xx in obj.items():
                    self._add(xx)
            elif not isinstance(obj, str):
                self._add(xx)



    def extend(self, *args):
        for i in args:
            self._add(i)

    def print_sum(self):
        print(f'Переменные функции заняли {self._sum_mem} байт памяти')




b = revers_1(a)
n = int(a)
rev = ''
while True:
    rev += str(n % 10)
    n //= 10
    if n == 0:
        break

summary1 = ShowSize()
summary1.extend(a, n, rev)
summary1.print_sum()

print(struct.unpack('LLLLlL' + 'c' * (len(b) + 1), ctypes.string_at(id(b), sys.getsizeof(b))))

print('*' * 50)

b = revers_2(a)
res = ''
for i in a[::-1]:
    res += i

summary2 = ShowSize()
summary2.extend(a, res)
summary2.print_sum()
print(struct.unpack('LLLLlL' + 'c' * (len(b) + 1), ctypes.string_at(id(b), sys.getsizeof(b))))

print('*' * 50)

b = revers_3(a)
c = a[::-1]

summary3 = ShowSize()
summary3.extend(a, c)
summary3.print_sum()
print(struct.unpack('LLLLlL' + 'c' * (len(b) + 1), ctypes.string_at(id(b), sys.getsizeof(b))))

# Переменные функции заняли 140 байт памяти
# (1, 4487885904, 9, 18446744073709551615, 140197267305444, 0, b'9', b'8', b'7', b'6', b'5', b'4', b'3', b'2', b'1', b'\x00')
# **************************************************
# Переменные функции заняли 116 байт памяти
# (1, 4487885904, 9, 18446744073709551615, 228, 0, b'9', b'8', b'7', b'6', b'5', b'4', b'3', b'2', b'1', b'\x00')
# **************************************************
# Переменные функции заняли 116 байт памяти
# (1, 4487885904, 9, 18446744073709551615, 228, 0, b'9', b'8', b'7', b'6', b'5', b'4', b'3', b'2', b'1', b'\x00')

print(sys.getsizeof(a), sys.getsizeof(b))

'''Переменные первой функции заняли 140 байт, но длительность была выше вероятно за счет дополнительных арифметических действий.
Переменные 2ой и 3ей функции заняли по 116 байт. Исходная и конечная переменные весят 58 байт'''

