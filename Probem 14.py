""" Самая длинная последовательность Коллатца
Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?"""

rez = {}


def get_step_collatz(arr: dict, step: int) -> int:
    if step == 1:
        return 1
    if step % 2 == 0:
        next_step = step / 2
    else:
        next_step = step * 3 + 1
    if next_step in arr:
        return 1 + arr[next_step]
    else:
        return 1 + get_step_collatz(arr, next_step)


for i in range(2, 1000000):
    rez[i] = get_step_collatz(rez, i)

print(max(rez.values()))

print(list(rez.keys())[list(rez.values()).index(max(rez.values()))])

