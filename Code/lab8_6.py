# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 3 - 2

# Выполнить транспонирование квадратной матрицы.


# Input matrix
n = int(input("Введите порядок матрицы: "))     # matrix order
if n < 0:
    print("Порядок матрицы должен > 0!")
    exit()

# matrix
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input(f'Введите элемент A[{i}][{j}]: '))

# output
print("Введенная матрица: ")
for i in range(n):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()


# Transpose
for i in range(n):
    for j in range(i, n):
        a[i][j], a[j][i] = a[j][i], a[i][j]


# Output
print("Измененная матрица: ")
for i in range(n):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()