# Квадратное диофантово уравнение

x = 15
n = 21

while n < 10 ** 12:
    x_step = 3 * x + 2 * n - 2
    n_step = 4 * x + 3 * n - 3

    x = x_step
    n = n_step

print(x)
