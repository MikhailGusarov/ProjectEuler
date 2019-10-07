import math
res = [0] * 1001
for i in range(1,1000):
    for j in range(i,1000):
        k = math.sqrt(i ** 2 + j ** 2)
        if i + j + k > 1000:
            break
        if k != round(k):
            continue
        res[int(i+j+k)] += 1
        
print(res.index(max(res)))
