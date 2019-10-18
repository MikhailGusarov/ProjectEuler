x = 28433
diff = 7830457
for i in range(diff):
	x *=2
	if len(str(x)) > 10:
		x =int(''.join( list(str(x))[len(str(x))-10:]))

print(x+1)