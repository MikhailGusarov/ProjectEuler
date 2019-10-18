from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    counter = 5
    while (counter ** 2) <= n:
        if n % counter == 0:
            return False
        if n % (counter + 2) == 0:
            return False
        counter += 6
    return True


res = []

for i in range(3, 1000):
    if not is_prime(i):
        continue
    for j in range(7, 1001):
        if not is_prime(j):
            continue
        for k in range(j + 1, 1002):
            if not is_prime(k):
                continue
            for g in range(k + 1, 1003):
                if not is_prime(g):
                    continue
                for l in range(g + 1, 1004):
                    if not is_prime(l):
                        continue
                    count = 0
                    for m in set(permutations([str(i), str(j), str(k), str(g), str(l)], 2)):
                        if not is_prime(int(''.join(m))):
                            break
                        else:
                            count += 1
                    if count == 20:
                        res.append(i+j+k+g+l)
                        print(i+j+k+g+l)
                        break


