res = 0
for i in range(2, 10000000):
    if i == 89:
        res += 1
        continue
    x = sum([int(j) ** 2 for j in str(i)])
    while x != 1:
        if x == 89:
            res += 1
            break
        x = sum([int(j) ** 2 for j in str(x)])
print(res)
