num = 1
den = 1

for i in range(10,100):
    if i % 10 == 0:
        continue
    for j in range(i+1,100):
        if j % 10 == 0:
            continue
        for k in str(i):
            if k in str(j):
                x = str(i).replace(k,'')
                y = str(j).replace(k,'')
                if x and y:
                    if int(x) * j == int(y) * i:
                        num *= int(x)
                        den *= int(y)

print(int(den/num))
