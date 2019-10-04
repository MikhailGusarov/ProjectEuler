arr = [2]
flg = 0
res = 0
for i in range(3, 1000000):
    for j in arr:
        if i % j == 0:
            break
        elif j ** 2 >= i:
            arr.append(i)
            break

for i in arr:
    if '0' in str(i):
        continue
    if len(str(i)) == 1:
        res += 1
        print(i)
        continue
    count = 0
    x = i
    for j in range(len(str(i))-1):
        x = int(str(x)[1:] + str(x)[0])
        if x not in arr:
            break
        else:
            count += 1
    if count == len(str(i)) - 1:
        res += 1
        print(i)

print(res)
