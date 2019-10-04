import itertools
arr = (list(itertools.permutations(range(1, 10))))
res = set()
for i in arr:
    arr_step = list(map(str, i))
    if int(''.join(arr_step[:2])) * int(''.join(arr_step[2:5])) == int(''.join(arr_step[5:])) or \
            int(''.join(arr_step[:1])) * int(''.join(arr_step[1:5])) == int(''.join(arr_step[5:])):
        res.add(int(''.join(arr_step[5:])))

print(sum(res))