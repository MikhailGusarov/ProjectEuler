from itertools import permutations

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



arr = ['2']
for i in range(3,100,2):
    for j in arr:
        if int(j) ** 2 > i:
            arr.append(str(i))
            break
        if i % int(j) == 0:
            break
