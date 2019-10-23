import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


d = 12000

res = {}

for i in range(d, 3, -1):
    num_step_down = int(i / 3) + 1
    num_step_up = math.ceil(i / 2)
    for j in range(num_step_down, num_step_up):
        step = i / gcd(i, j)
        if step in res.keys():
            res[step].add(j / gcd(i, j))
        else:
            res[step] = {j / gcd(i, j)}
count = 0
for i in res:
    count += len(res[i])

print(count)
