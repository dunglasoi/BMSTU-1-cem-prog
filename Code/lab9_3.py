# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Подсчитать в каждой строке матрицы D количество элементов,
# превышающих суммы элементов соответствующих строк матрицы Z.
# Разместить эти количества в массиве G,
# умножить матрицу D на максимальный элемент массива G.
#
# Напечатать матрицу Z, матрицу D до и после преобразования, а также массив G.


WIDTH = 11          # output format width


# Input
row_d = int(input("Введите количество строк матрицы D: "))      # matrix D rows
if row_d < 0:
    print("Количество строк матрицы D должно > 0!")
    exit()

col_d = int(input("Введите количество столбцов матрицы D: "))   # matrix D columns
if col_d < 0:
    print("Количество столбцов матрицы D должно > 0!")
    exit()

row_z = int(input("Введите количество строк матрицы Z: "))       # matrix Z rows
if row_z < 0:
    print("Количество строк матрицы Z должно > 0!")
    exit()

col_z = int(input("Введите количество столбцов матрицы Z: "))     # matrix Z columns
if col_z < 0:
    print("Количество столбцов матрицы Z должно > 0!")
    exit()

# matrix D
print("Введите элемент D матрицы:")
a_d = [[int(input(f"D[{i}][{j}]: ")) for j in range(col_d)]
       for i in range(row_d)]

# matrix Z
print("Введите элемент Z матрицы:")
a_z = [[int(input(f"Z[{i}][{j}]: ")) for j in range(col_z)]
       for i in range(row_z)]

# output Z
print("Z матрица:")
for i in range(row_z):
    for j in range(col_z):
        print(f'{a_z[i][j]:^{WIDTH}g}', end=' ')
    print()

# output D pre transformation
print("D матрица до преобразования:")
for i in range(row_d):
    for j in range(col_d):
        print(f'{a_d[i][j]:^{WIDTH}g}', end=' ')
    print()

# matrix G
a_g = []
col_g = min(row_d, row_z)       # vector G columns
max_g = 0                       # max G element
for i in range(col_g):
    s = sum(a_z[i])   # sum z[i] row
    a_g.append(0)
    for j in range(col_d):
        if a_d[i][j] > s:
            a_g[i] += 1

    if a_g[i] > max_g:
        max_g = a_g[i]

# transform matrix D
for i in range(row_d):
    for j in range(col_d):
        a_d[i][j] *= max_g

# output D after transformation
print("D матрица после преобразования:")
for i in range(row_d):
    for j in range(col_d):
        print(f'{a_d[i][j]:^{WIDTH}g}', end=' ')
    print()

# output G
print("G матрица:")
for i in range(col_g):
    print(f'{a_g[i]:^{WIDTH}g}', end=' ')
print()