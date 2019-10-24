def factors(x):
    res = 0
    for i in range(1, x + 1):
        if x % i == 0:
            res += i
    res -= - x
    return res


res = []
for i in range(2, 200000):
    res.append([i])
    x = factors(i)
    # print(i)
    while True:
        # print(x)
        if x == i:
            break
        if x > 1000000 or len(res[len(res)-1]) > 100:
            res.pop()
            break
        else:
            res[len(res) - 1].append(x)
        x = factors(x)
max_len = 0
min_val = 0
for i in res:
    if max_len < len(i):
        print(i)
        max_len = len(i)
        min_val = min(i)
print(min_val)
