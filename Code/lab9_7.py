# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Ввести трёхмерный массив (массив матриц размера X*Y*Z),
# вывести из него i-й срез (матрицу - фрагмент трёхмерного массива)
# по второму индексу (нумерация индексов начинается с 1).


WIDTH = 11          # output format width


# Inputs
rows = int(input("Введите количество строк матрицы: "))        # matrix rows
if rows < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

cols = int(input("Введите количество столбцов матрицы: "))     # matrix columns
if cols < 0:
    print("Количество столбцов матрицы должно > 0!")
    exit()

pages = int(input("Введите количество страниц матрицы: "))      # matrix pages
if pages < 0:
    print("Количество столбцов страниц должно > 0!")
    exit()

# input element
print("Введите элемент матрицы:")
a = [[[int(input(f"A[{i}][{j}][{k}]: ")) for k in range(pages)]
      for j in range(cols)]
     for i in range(rows)]

# output matrix
print("Введенная матрица:")
for i in range(rows):
    for j in range(cols):
        for k in range(pages):
            print(f'{a[i][j][k]:^{WIDTH}g}', end=' ')
        print()
    print()


# Slice
s = -1          # slice
while True:
    s = int(input("Введите i-й срез: "))
    if 0 <= s < cols:
        break
    print(f"i-й срез должен >= 0 и < {cols}!")

# output slice
for i in range(rows):
    for k in range(pages):
        print(f'{a[i][s][k]:^{WIDTH}g}', end=' ')
    print()


# 1 2
# 3 4

# 4 3
# 2 1