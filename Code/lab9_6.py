# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B),
# потом сложить все элементы в столбцах матрицы C и записать их в массив V.
#
# Напечатать матрицы A, B, C и массив V.

WIDTH = 11          # output format width

# Input
row = int(input("Введите количество строк матрицы: "))      # matrix rows
if row < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

col = int(input("Введите количество столбцов матрицы: "))   # matrix columns
if col < 0:
    print("Количество столбцов матрицы должно > 0!")
    exit()

# matrix A
print("Введите элемент A матрицы:")
a_a = [[float(input(f"A[{i}][{j}]: ")) for j in range(col)]
       for i in range(row)]

# matrix B
print("Введите элемент B матрицы:")
a_b = [[float(input(f"B[{i}][{j}]: ")) for j in range(col)]
       for i in range(row)]

# matrix C
a_c = [[a_a[i][j]*a_b[i][j] for j in range(col)]
       for i in range(row)]

# vector V
a_v = [sum([r[i] for r in a_c]) for i in range(col)]


# output A
print("A матрица:")
for i in range(row):
    for j in range(col):
        print(f'{a_a[i][j]:^{WIDTH}g}', end=' ')
    print()

# output B
print("B матрица:")
for i in range(row):
    for j in range(col):
        print(f'{a_b[i][j]:^{WIDTH}g}', end=' ')
    print()

# output C
print("C матрица:")
for i in range(row):
    for j in range(col):
        print(f'{a_c[i][j]:^{WIDTH}g}', end=' ')
    print()

# output V
print("V массив:")
for i in range(col):
    print(f'{a_v[i]:^{WIDTH}g}', end=' ')
print()