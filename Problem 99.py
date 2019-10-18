import math
arr = []
with open('Problem 99 base_exp.txt') as data:
    for i in data:
        x = i.replace('\n','').split(',')
        if x != []:
            arr.append(x)


res = 0
for i in range(1, len(arr)):
    #print(i)
    x = int(arr[res][0])
    x_diff = int(arr[res][1])
    y = int(arr[i][0])
    y_diff = int(arr[i][1])

    while (y_diff != x_diff) and (y_diff != 1 and x_diff != 1):
        #print(x_diff, y_diff)
        if x_diff > y_diff:
            x_diff -= y_diff
            y /= x
        else:
            y_diff -= x_diff
            x /= y
    if y > x:
        res = i

print(res + 1)
    
