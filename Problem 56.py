res =0
for a in range(100):
	for b in range(100):
		x = [int(k) for k in str(a**b)]
		if sum(x) > res:
			res = sum(x)
print(res)