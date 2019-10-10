arr_simple = [2]
for i in range(3,1000000,2):
    for j in arr_simple:
        if j**2 > i:
            arr_simple.append(i)
            break
        if i % j == 0:
            break

res = 0
count = 0

for i in range(len(arr_simple)):
    for j in range(i,len(arr_simple)):
        if count > j-i:
            continue
        if sum(arr_simple[i:j+1]) in arr_simple:
            res = sum(arr_simple[i:j+1])
            count = j-i
        if sum(arr_simple[i:j+1]) > 1000000:
            break
print(res)
