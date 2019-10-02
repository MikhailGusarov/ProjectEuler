dict_num = {}
num = 28123

# запишем сумму всех делителей в словарь
for i in range(12, num - 12 + 1):
    dict_num[i] = {1}
    for j in range(2, i):
        if j ** 2 > i:
            break
        if i % j == 0:
            dict_num[i].add(j)
            dict_num[i].add(int(i/j))
    dict_num[i] = sum(dict_num[i])

arr = [i for i, j in dict_num.items() if i < j]

res = set(range(0, num))

nun = set()

for i in range(len(arr)):
    for j in range(i, len(arr)):
        nun.add(arr[i] + arr[j])

res = res.difference(nun)
print(nun)
print(sum(res))
