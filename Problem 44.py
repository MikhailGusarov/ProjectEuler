import math
arr = [n*(3*n-1)/2 for n in range(1,5000)]
res = []

for i in range(len(arr)):
	for j in range(i,len(arr)):
		if (math.sqrt(24*(arr[j] + arr[i])+1)+1)/6 == (math.sqrt(24*(arr[j] + arr[i])+1)+1)//6 :
			if (math.sqrt(24*(arr[j] - arr[i])+1)+1)/6 == (math.sqrt(24*(arr[j] -arr[i])+1)+1)//6 :
				res.append(arr[j]-arr[i])
print(min(res))