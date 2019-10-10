arr_simple = [2]
for i in range(3,20000,2):
    flg = 0
    for j in arr_simple:
        if i % j == 0:
            flg = 1
            break
    if flg == 0:
        arr_simple.append(i)

res = set()


for i in range(100000, 140000):
    if i in arr_simple:
        continue
    count = 0
    for j in arr_simple:
        if i % j == 0:
            count += 1
        if count > 3:
            res.add(i)
            break

res = list(res)
res.sort()
for i in range(len(res) - 3):
    if res[i] == res[i + 3] - 3:
        print(res[i])
        break
