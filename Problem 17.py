import num2words

num = 1000
rez = 0

for i in range(1, num + 1):
    rez += len(num2words.num2words(i).replace(' ', '').replace('-', ''))


print(rez)


