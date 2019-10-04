from math import factorial

res = 0
for i in range(3, 100000):
    step = 0
    for j in str(i):
        step += factorial(int(j))
    if i == step:
        res += i
print(res)
