res = {}
for i in range(22, 10000):
    step = list(str(i ** 3))
    step.sort()
    step = ''.join(step)
    if step in res.keys():
        res[step].append(i)
    else:
        res[step] = [i]

for i in res:
    if len(res[i]) == 5:
        print(min(res[i])**3)
        break

