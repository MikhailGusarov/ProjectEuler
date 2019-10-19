import math
dict_break = {169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2, 145: 100, 2: 100, 40585: 100}
count_res = 0

for i in range(70, 1000000):
    count = 0
    x = sum([math.factorial(int(j)) for j in str(i)])
    while x not in dict_break.keys():
        # print(x)
        count += 1
        x = sum([math.factorial(int(j)) for j in str(x)])
    count += dict_break[x]
    if count == 60:
        count_res += 1
print(count_res)
