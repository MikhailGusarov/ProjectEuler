with open('Problem 81 matrix.txt') as data:
    arr = [i.replace("\n", "").split(",") for i in data]
arr = [[int(j) for j in i] for i in arr]

# arr = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

len_arr = len(arr)
arr_res = [[0 for j in range(len_arr)] for i in range(len_arr)]
arr_res[0][0] = arr[0][0]


for i in range(len_arr):
    for j in range(len_arr):
        if j != len_arr-1 and (arr_res[i][j+1] == 0 or arr_res[i][j+1] > arr_res[i][j] + arr[i][j+1]):
            arr_res[i][j + 1] = arr_res[i][j] + arr[i][j + 1]
        if i != len_arr-1 and (arr_res[i+1][j] == 0 or arr_res[i+1][j] > arr_res[i][j] + arr[i+1][j]):
            arr_res[i+1][j] = arr_res[i][j] + arr[i+1][j]

print(arr_res[len_arr-1][len_arr-1])
