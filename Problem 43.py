import itertools
arr_simple = [1, 2, 3, 5, 7, 11, 13, 17]
x = []
y = '012345678'
for i in range(9,10):
    y += str(i)
    x += list(itertools.permutations(y))
x = {''.join(i) for i in x if i[0] != '0'}

res = 0

for i in x:
    count = 0
    for j in range(0, len(i) - 2):
        if int(i[j] + i[j+1] + i[j+2]) % arr_simple[j] !=0:
            count = 0
            break
        else:
            count = 1
    if count:
        res += int(i)

print(res)
        
            



