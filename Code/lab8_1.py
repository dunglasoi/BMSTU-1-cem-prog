# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 3 - 2

# Найти строку, имеющую определённое свойство по варианту.
# Наименьшее количество чётных элементов.


# input matrix
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

# output matrix
print("Введенная матрица: ")
for i in range(m):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()


# find
min = n     # min even element
b = []      # array 'min element' rows
for i in range(m):
    cur = 0     # current even element
    for j in range(n):
        if a[i][j] % 2 == 0:
            cur += 1
    if cur < min:
        min = cur
        b = [a[i]]
    elif cur == min:
        b += [a[i]]


# Output matrix after finding
print("Строки с наименьшими четных элементов: ")
for i in range(len(b)):
    for j in range(n):
        print("{:^5g}".format(b[i][j]), end=' ')
    print()