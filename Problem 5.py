"""2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?"""

count = 20

a = [i for i in range(1, count+1)]

for i in range(count):
    for j in range(i, count):
        if a[j] % a[i] == 0 and i != j:
            a[j] /= a[i]
res = 1
for i in a:
    res *= i

print(res)
