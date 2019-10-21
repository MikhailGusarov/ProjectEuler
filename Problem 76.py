# Как задача с монетами из 31 проблемы

amount = 100
coins = list(range(1, 100))
count_change = [1] + [0] * amount

# цикл по монетам
for i in range(len(coins)):
    # цикл от текущей монеты до максимального значения
    for j in range(coins[i], amount+1):
        # кол-во изменений на итерации = кол-во изм. нап предыдущей итерации.
        # + кол-во изменений элемента j - текущая монета
        count_change[j] += count_change[j - coins[i]]

print(max(count_change))
