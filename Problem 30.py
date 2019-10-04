arr = []

for i in range(12, 999999):
	sum_j = 0
	for j in str(i):
		sum_j += int(j) ** 5
	if i == sum_j:
		arr.append(i)
		
print(sum(arr))
