""" Произведение простых чисел меньше 1млн"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


count_max = 0
res = 0
for i in range(510510, 510512, 2):
    count = 0
    for j in range(1, i):
        if gcd(i, j) == 1:
            count += 1
    if count_max < i / count:
        count_max = i / count
        res = i
    # print(i, count, i/count)
print(res, count_max)
