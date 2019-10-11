res = []
for i in range(12, 10000):
	step = i
	for j in range(50):
		y = list(str(step))
		y.reverse()
		y = int(''.join(y))
		z = list(str(step+ y))
		z.reverse()
		if z != list(str(step+ y)) and j == 49:
			res.append(i)
			break
		if z != list(str(step+ y)):
			step = step + y
		else:
			break
			
print(len(res))
			