for i in range(1, 10000000):
    x1 = list(set(str(2 * i)))
    x1.sort()
    x2 = list(set(str(3 * i)))
    x2.sort()
    x3 = list(set(str(4 * i)))
    x3.sort()
    x4 = list(set(str(5 * i)))
    x4.sort()
    x5 = list(set(str(6 * i)))
    x5.sort()
    if x1 == x2 == x3 == x4 == x5:
        print(i)
        break
