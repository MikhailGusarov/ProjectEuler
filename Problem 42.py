letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
with open('Problem 42 words.txt') as data:
    arr = data.readline().replace('"', '').split(',')
count = 0
arr_qty = [int(i/2*(i+1)) for i in range(1, 1000)]

for word in arr:
    count_word = 0
    for j in word:
        count_word += (letters.index(j)+1)
    if count_word in arr_qty:
        count += 1

print(count)
