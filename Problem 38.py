res = []
arr_num = list('123456789')
for i in range(9,10000):
    if str(i)[0] != '9':
        continue
    x = ''
    j = 1
    while len(x) < 9:
        x += str(i * j)
        j += 1
    if len(x) == 9:
        x_arr = list(x)
        x_arr.sort()
        if x_arr == arr_num:
            res.append(int(x))
print(max(res))
