# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 3 - 2

# Переставить местами столбцы с максимальной и минимальной суммой элементов.


# Input matrix
m = int(input("Введите количество строк матрицы: "))         # number of rows
if m < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

n = int(input("Введите количество столбцов матрицы: "))      # number of columns
if n < 0:
    print("Количество столбцов матрицы должно > 0!")
    exit()

# matrix
a = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input(f'Введите элемент A[{i}][{j}]: '))

# output
print("Введенная матрица: ")
for i in range(m):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()


# find
min = 0     # min sum
for i in range(m):
    min += a[i][0]
max = 0     # max sum
for i in range(m):
    max += a[i][0]
i_min = 0   # index column with min sum
i_max = 0   # index column with max sum

for j in range(n):
    cur = 0     # current sum
    for i in range(m):
        cur += a[i][j]

    if cur < min:
        min = cur
        i_min = j
    if cur > max:
        max = cur
        i_max = j

# swap element
for i in range(m):
    a[i][i_min], a[i][i_max] = a[i][i_max], a[i][i_min]


# Output
print("Измененная матрица: ")
for i in range(m):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()