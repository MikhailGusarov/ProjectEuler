res = 0
pmax = 0

for i in range(3, 1000, 2):
    if i % 5 == 0:
        continue
    p = 1
    while (10 ** p) % i != 1:
        p +=1

    if p > pmax:
        res = i
        pmax = p

print(res)
    



