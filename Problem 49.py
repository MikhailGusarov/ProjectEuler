import itertools
arr_simple = [2]
for i in range(3,10000,2):
    flg = 0
    for j in arr_simple:
        if i % j == 0:
            flg = 1
            break
    if flg == 0:
        arr_simple.append(i)

arr = []

for i in range(len(arr_simple)):
    if arr_simple[i]> 1000:
        arr = arr_simple[i:]
        break
res = []
for i in arr:
    x = set(itertools.permutations(str(i)))
    res_x = list({int(''.join(j)) for j in x if int(''.join(j)) in arr})
    res_x.sort()
    if len(res_x) >= 3:
        for j in range(len(res_x)-2):
            if res_x[j+1] +(res_x[j+1] - res_x[j]) in res_x:
                print(res_x[j],res_x[j+1],res_x[j+2])
                break

