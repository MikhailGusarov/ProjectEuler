import itertools
x = []
y = '123'
for i in range(4, 10):
    y += str(i)
    x += list(itertools.permutations(y))
x = [int(''.join(i)) for i in x if int(''.join(i)) % 2 != 0 ]
x.sort()
x.reverse()
simple_arr = [2]

for i in range(3,1000000, 2):
    for j in simple_arr:
        if i % j == 0:
            break
        if j ** 2 > i:
            simple_arr.append(i)
            count = len(x)
            for k in range(count):
                if k >= len(x):
                    break
                if x[k] % i == 0:
                    x.pop(k)
            break
print(max(x), len(x))
