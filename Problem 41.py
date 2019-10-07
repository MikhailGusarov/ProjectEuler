import itertools
x = []
y = '123'
for i in range(4,9):
    y += str(i)
    x += list(itertools.permutations(y))
x = [int(''.join(i)) for i in x if int(''.join(i)) % 2 != 0 ]
x.sort()
x.reverse()
simple_arr = [2]
 
for i in range(3,35000, 2):
    for j in simple_arr:
        if i % j == 0:
            break
        if j ** 2 > i:
            simple_arr.append(i)
            break

while x !=[]:
	x_step = x[0]
	for i in simple_arr:
		if x[0] % i == 0:
			x.pop(0)
			break
	if x[0] == x_step:
		break
	

print(max(x),len(x))
