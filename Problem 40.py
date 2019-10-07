str_num = ''.join([str(i) for i in range(1000001)])
i = 1
res = 1
while i != 1000000:
    res *= int(str_num[i])
    i *= 10
print(res)
