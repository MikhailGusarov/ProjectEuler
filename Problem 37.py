res = []
simple_arr =[2]
for i in range(3, 1000000,2):
 for j in simple_arr:
  if i % j == 0:
   break
  if j ** 2 > i:
   simple_arr.append(i)
   for k in range(1, len(str(i))):
    if int(str(i)[k:]) not in simple_arr or int(str(i)[:k]) not in simple_arr:
     break
    if k ==  len(str(i))- 1:
     res.append(i)
   break
   
print(sum(res))
