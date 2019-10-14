with open('Problem 59 cipher.txt') as data:
    arr = data.readline().split(',')
arr = [int(i) for i in arr]



for i in range(97,123):
    for j in range(97,123):
        for z in range(97,123):
            arr_key = [i, j, z] * int((len(arr) / 3))
            res_step = ''.join([chr(arr[k] ^ arr_key[k]) for k in range(len(arr))])
            if res_step[0] == '(':
                print(res_step)
                
