import math
n = 10
arr = list(range(n))

x = 999999

ans = ''
for i in range(1, n):
    res = x // math.factorial(n - i)
    ans += str(arr.pop(res))
    x = x - res * math.factorial(n - i)


ans += str(arr.pop())
print(ans)
