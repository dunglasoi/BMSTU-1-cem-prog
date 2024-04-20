# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 3 - 2

# Переставить местами строки с наибольшим и наименьшим
# количеством отрицательных элементов.


# Input matrix
m = int(input("Введите количество строк матрицы: "))          # number of rows
if m < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

n = int(input("Введите количество столбцов матрицы: "))       # number of columns
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
min = n     # min negative element
max = 0     # max positive element
i_min = 0   # index row with min negative element
i_max = 0   # index row with max negative element

for i in range(m):
    cur = 0     # current negative element
    for j in range(n):
        if a[i][j] < 0:
            cur += 1

    if cur < min:
        min = cur
        i_min = i
    if cur > max:
        max = cur
        i_max = i

# swap element
for i in range(n):
    a[i_min][i], a[i_max][i] = a[i_max][i], a[i_min][i]


# Output
print("Измененная матрица: ")
for i in range(m):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()