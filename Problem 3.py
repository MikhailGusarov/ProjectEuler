"""Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?"""
number = 600851475143
divider = 2
while divider != number:
	if number % divider == 0:
		number = number / divider
	else:
		divider = divider + 1
print(int(number))
