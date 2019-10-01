day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# проверка на високосный год
def is_leap_year(year):
    if year % 400 == 0 and str(year)[2:4] == '00':
        return True
    if year % 4 == 0 and str(year)[2:4] != '00':
        return True
    return False


if is_leap_year(1900):
    day_of_month[1] += 1

# 1 - понедельник, 7 - воскресенье
start = (1 + 365) % 7

count_sunday = 0


for i in range(1901, 2001):
    if is_leap_year(1900):
        day_of_month[1] = 29
    else:
        day_of_month[1] = 28
    for j in day_of_month:
        start += j
        if start % 7 == 0:
            count_sunday += 1

print(count_sunday)
