res = 0
for i in range(1,10):
    for j in range(100):
        if len(str(i ** j)) == j:
            res +=1
print(res)
