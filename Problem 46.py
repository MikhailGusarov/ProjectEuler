arr_pow = [2 * i ** 2 for i in range(1, 60)]
arr_simple = [2]
arr_not_simple = []
count = 0
for i in range(3, 10000, 2):
    count = 0
    for j in arr_simple:
        if i % j == 0:
            arr_not_simple.append(i)
            count = 1
            break
    if count == 0:
        arr_simple.append(i)

for i in arr_simple:
    for j in arr_pow:
        if (j + i) in arr_not_simple:
            arr_not_simple[arr_not_simple.index(j+i)] = 0

print(min([i for i in arr_not_simple if i != 0]))
