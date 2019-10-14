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

max_num = 1
count = 1
count_simple = 0
len = 100001


for i in range(3, len + 1, 2):
    for j in range(4):
        if isPrime(max_num + i - 1):
           count_simple += 1
        max_num += i -1
        count += 1
    if count_simple / count < 0.1:
        print(count // 2 + 1)
        break


