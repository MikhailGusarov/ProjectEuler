res_a = -999
res_b = -1000
res_n = 0

numer = 20000
x = 0
arr = list(range(2, numer))

while arr[x] ** 2 < numer:
    arr = arr[:x + 1] + [i for i in arr[x+1:] if i % arr[x] != 0]
    x += 1



for a in range(-999, 1000, 1):
    if a == 0:
        continue
    for b in range(-1000, 1001, 1):
        n = 0
        if b == 0:
            continue
        while (n ** 2 + a * n + b) in arr:
            if (n ** 2 + a * n + b) <= 0:
                break
            n +=  1
        if n > res_n:
            res_n = n
            res_a = a
            res_b = b

print(res_a * res_b)

