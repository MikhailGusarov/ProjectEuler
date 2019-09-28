"""Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc."""

import math


def special_three_pythagoras() -> int:
    for i in range(1, 999):
        for j in range(i, 1000):
            c = math.sqrt(i ** 2 + j ** 2)
            if int(c) != c:
                continue
            if i + j + c == 1000:
                return i * j * int(c)


print(special_three_pythagoras())

