"""Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов."""

arr = [2]
num = 3

while num < 200000:
    for i in arr:
        if num % i == 0:
            break
        elif num % i != 0 and i == arr[len(arr)-1]:
            arr.append(num)
    num += 2
print(sum(arr))

