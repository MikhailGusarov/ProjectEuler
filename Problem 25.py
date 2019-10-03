arr =[1, 1]
index_res = 0
for i in range(10000000):
	arr.append(arr[i + 1] + arr[i])
	if len(str(arr[i + 2])) == 1000:
		index_res = i + 2
		break
print(index_res)
