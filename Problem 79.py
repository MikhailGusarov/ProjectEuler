with open('Problem 79 keylog.txt') as data:
    arr = [list(i.strip()) for i in data]

res = []

while arr != []:
    
    x1 = []
    x2 = []

    for i in range(10):
        if i in x1:
            continue
        for j in arr:
            if j == []:
                continue
            if int(j[0]) == i:
                x1.append(i)
                break
        
    for i in range(10):
        if i in x2:
            continue
        for j in arr:
            if len(j) < 2:
                continue
            if int(j[1]) == i:
                x2.append(i)
                break
    print(list(set(x1).difference(x2)))    
    step = list(set(x1).difference(x2))[0]
    res.append(step)
    len_arr = len(arr)
    for i in range(len_arr):
        if i >= len(arr):
            break
        if len(arr[i]) == 3 and int(arr[i][2]) == step:
            arr[i]=arr[i][:2]
        if len(arr[i]) == 2 and int(arr[i][1]) == step:
            arr[i]=[arr[i][0],arr[i][2]]   
        if int(arr[i][0]) == step:
            arr[i]=arr[i][1:]
            if  arr[i] == []:
                arr.pop(i)

# 73162890
