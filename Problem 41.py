import itertools
x = []
y = '123'
for i in range(4,10):
    y += str(i)
    x += list(itertools.permutations(y))

simple_arr = [2]

for i in range(3,1000000, 2):
    for j in simple_arr:
        if i % j == 0:
            break
        if j ** 2 > i:
            simple_arr.append(i)
            break
