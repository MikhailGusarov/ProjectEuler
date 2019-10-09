import math
arr =[n*(2*n-1) for n in range(144,10000000)]
res =0
for i in arr:
	if (math.sqrt(24*i+1)+1)/6 ==(math.sqrt(24*i+1)+1)//6 and (math.sqrt(8*i +1)-1)/2 == (math.sqrt(8*i +1)-1)//2:
		res=i
		break
print(res)