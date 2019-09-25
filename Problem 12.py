triangle = [sum(range(i)) for i in range(2, 14000, 1)]
res = 0

for i in triangle:
    count = 0
    if i == 1:
        continue
    for j in range(1, i):
        if j ** 2 > i:
            break
        if i % j == 0:
            count += 2

    if count > 500:
        res = i
        break

print(res)
