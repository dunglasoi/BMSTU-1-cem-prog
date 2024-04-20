# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой стрелке,
# затем на 90 градусов против часовой стрелки.
#
# Вывести исходную, промежуточную и итоговую матрицы.
#
# Дополнительных матриц и массивов не вводить. Транспонирование не применять.


WIDTH = 11          # output format width


# Input matrix
n = int(input("Введите порядок матрицы: "))    # matrix order
if n < 0:
    print("Порядок матрицы должен > 0!")
    exit()

# matrix A
a = [[int(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# output
print("Исходная матрица:")
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:^{WIDTH}g}', end=' ')
    print()


# Rotate 90 degree clockwise
for i in range(n//2):
    for j in range(i, n-i-1):
        # store current cell in tmp
        tmp = a[i][j]
        # move values from left to top
        a[i][j] = a[n-1-j][i]
        # move values from bottom to left
        a[n-1-j][i] = a[n-1-i][n-1-j]
        # move values from right to bottom
        a[n-1-i][n-1-j] = a[j][n-1-i]
        # assign tmp to right
        a[j][n-1-i] = tmp

print("Матрица после поворота на 90 градусов по часовой стрелке:")
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:^{WIDTH}g}', end=' ')
    print()


# Rotate 90 degree counter clockwise
for i in range(n//2):
    for j in range(i, n-i-1):
        # store current cell in tmp
        tmp = a[i][j]
        # move values from right to top
        a[i][j] = a[j][n-1-i]
        # move values from bottom to right
        a[j][n-1-i] = a[n-1-i][n-1-j]
        # move values from left to bottom
        a[n-1-i][n-1-j] = a[n-1-j][i]
        # assign tmp to left
        a[n-1-j][i] = tmp

print("Матрица после поворота на 90 градусов против часовой стрелке:")
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:^{WIDTH}g}', end=' ')
    print()