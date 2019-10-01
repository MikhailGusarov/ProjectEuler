dict_num = {}

num = 10000

# запишем сумму всех делителей в словарь
for i in range(4, num):
    dict_num[i] = {1}
    for j in range(2, i):
        if j ** 2 > i:
            break
        if i % j == 0:
            dict_num[i].add(j)
            dict_num[i].add(int(i/j))
    dict_num[i] = sum(dict_num[i])

# сделаем проверку и выведем результат
res = 0

for i, j in dict_num.items():
    if (i < 4) or (j < 4) or (j >= num):
        continue
    if i != j and dict_num[i] == j and dict_num[j] == i:
        res += dict_num[i]

print(res)
