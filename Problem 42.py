letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
word = 'SKY'
count =0
arr_qty = [i/2*(i+1) for i in range(1,10000)]

count_word = 0
for i in word:
	count_word += letters.index(i)+1
if count_word in arr_qty:
	count +=1
	
print(count)