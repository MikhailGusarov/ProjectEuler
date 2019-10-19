with open('Problem 81 matrix.txt') as data:
    arr = [i.replace("\n", "").split(",") for i in data]
print(arr[0])