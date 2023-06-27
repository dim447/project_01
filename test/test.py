# row = int(input())
# col = int(input())
# n = 0
# if row * col < 9:
#     tab = 1
# elif row * col > 9 and row * col < 99:
#     tab = 2
# else:
#     tab = 3
# for i in range(1, row + 1):
#     for k in range(col + 1, 1):
#         print(f"{(k + n):{tab}}", end=' ')
#     n = n + col
#     print()

num = int(input())
col_with = int(input())
if num ** 2 < 9:
    tab = 1
elif num ** 2 > 9 and row * col < 99:
    tab = 2
else:
    tab = 3
for row in range(1, num + 1):
    for column in range(1, num + 1):
        print(f'{row * column:{tab}} |', end='')
    # print('-' * (num * col_with), end='')
    print()