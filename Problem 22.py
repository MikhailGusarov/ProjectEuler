letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open('Problem 22 names.txt') as data:
    arr = data.readline().replace('"', '').split(',')
arr.sort()
res = 0

for i in range(len(arr)):
    alphabet_num = 0
    for j in range(len(arr[i])):
        alphabet_num += letters.index(arr[i][j]) + 1
    res += alphabet_num * (i + 1)
print(res)
