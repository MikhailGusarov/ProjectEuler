"""Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона."""

a = []
for i in range(1, 100000):
	if i < 3:
		a.append(i)
	else:
		a.append(a[i-3] + a[i-2])
print(sum(i for i in a if i % 2 == 0 and i < 4000000))

