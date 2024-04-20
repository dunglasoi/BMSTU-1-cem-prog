# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений.
#
# Напечатать матрицу D, массивы I и R, среднее арифметическое значение.


WIDTH = 11          # output format width
PREC = 7            # output format precision


# Input
row_d = int(input("Введите количество строк матрицы D: "))     # matrix D rows
if row_d < 0:
    print("Количество строк матрицы D должно > 0!")
    exit()

col_d = int(input("Введите количество столбцов матрицы D: "))   # matrix D columns
if col_d < 0:
    print("Количество столбцов матрицы D должно > 0!")
    exit()

col_i = int(input("Введите размер массива I: "))                 # vector I columns
if col_i < 0:
    print("Размер массива I должен > 0!")
    exit()

# matrix D
print("Введите элемент D матрицы:")
a_d = [[int(input(f"D[{i}][{j}]: ")) for j in range(col_d)]
       for i in range(row_d)]

# vector I
print("Введите элемент I массива:")
a_i = [-1]*col_i
for i in range(col_i):
    while True:
        a_i[i] = int(input(f"I[{i}]: "))
        if 0 <= a_i[i] < row_d:
            break
        print(f"Элемент массива должен >= 0 и < {row_d}")

# vector R
a_r = [max(a_d[a_i[i]]) for i in range(col_i)]

# mean R
mean_r = sum(a_r)/col_i


# output D
print("D матрица:")
for i in range(row_d):
    for j in range(col_d):
        print(f'{a_d[i][j]:^{WIDTH}g}', end=' ')
    print()

# output I
print("I массив:")
for i in range(col_i):
    print(f'{a_i[i]:^{WIDTH}g}', end=' ')
print()

# output R
print("R массив:")
for i in range(col_i):
    print(f'{a_r[i]:^{WIDTH}g}', end=' ')
print()

# output mean R
print(f"Среднее арифметическое: {mean_r:.{PREC}g}")