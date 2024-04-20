# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 3 - 2

# Найти столбец, имеющий определённое свойство по варианту.
#
# Наименьшее количество отрицательных элементов.


# Input matrix
m = int(input("Введите количество строк матрицы: "))        # number of rows
if m < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

n = int(input("Введите количество столбцов матрицы: "))     # number of columns
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


# Find
min = n      # min negative element
b = []      # array 'min element' columns
for j in range(n):
    cur = 0     # current negative element
    for i in range(m):
        if a[i][j] < 0:
            cur += 1
    if cur < min:
        min = cur
        b = [[row[j] for row in a]]
    elif cur == min:
        b += [[row[j] for row in a]]


# Output
print("Столбцы с наименьшими отрицательных элементов:")
for i in range(len(b)):
    for j in range(len(b[i])):
        print("{:^5g}".format(b[i][j]), end=' ')
    print()