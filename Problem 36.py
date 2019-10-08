res = 0
for i in range(1, 1000000, 2):
    x = list(str(i))
    y = list(str(i))
    y.reverse()
    if x != y:
        continue
    x = list(bin(i))[2:]
    y = list(bin(i))[2:]
    y.reverse()
    if x == y:
        res += i
print(res)
