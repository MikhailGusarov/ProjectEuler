arr = [1]
len = 1001

for i in range(3, len + 1, 2):
    for j in range(4):
        arr.append(max(arr) + i - 1)
print(sum(arr))
