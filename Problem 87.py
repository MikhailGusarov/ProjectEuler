def isPrime(n):
    if (n <= 1): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    if (n < 9): return True
    if (n % 3 == 0): return False
    counter = 5
    while (counter ** 2) <= n:
        if (n % counter == 0): return False
        if (n % (counter + 2) == 0): return False
        counter += 6
    return True


res = set()
num_max = 50000000
up_2 = int((num_max - 2 ** 3 - 2 ** 4) ** (1/2))
up_3 = int((num_max - 2 ** 2 - 2 ** 4) ** (1/3))
up_4 = int((num_max - 2 ** 3 - 2 ** 2) ** (1/4))
for i in range(2, up_4 + 1):
    if not isPrime(i):
        continue
    for j in range(2, up_3 + 1):
        if not isPrime(j):
            continue
        if (i ** 4 + j ** 3) > num_max:
            break
        for k in range(2, up_2 + 1):
            if not isPrime(k):
                continue
            if (i ** 4 + j ** 3 + k**2) <= num_max:
                res.add(i ** 4 + j ** 3 + k**2)
print(len(res))
