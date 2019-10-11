num= [1,3]
dem =[1,2]
count = 0

for i in range(2,1003):
	num.append((2*num[i-1]+num[i-2]))
	dem.append((2*dem[i-1]+dem[i-2]))
	if len(str(num[i]))  > len(str(dem[i])):
		count += 1
print(count)