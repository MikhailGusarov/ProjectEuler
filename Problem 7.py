"""Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?"""

arr = [2]
num = 3

while len(arr) != 10001:
    for i in range(len(arr)):
        if num % arr[i] == 0:
            break
        elif num % arr[i] != 0 and i == len(arr)-1:
            arr.append(num)        
    num += 1
print(max(arr))
