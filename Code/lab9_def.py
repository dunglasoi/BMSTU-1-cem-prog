# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б

WIDTH = 11

# input
n = int(input("Введите порядок матрицы: "))
if n < 0:
    print("Порядок матрицы должен > 0!")
    exit()

# matrix A
a = [[int(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# ouput
print("Исходная матрица:")
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:^{WIDTH}g}', end=' ')
    print()

# Rotate
for _ in range(2):
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

print("Матрица после поворота:")
for i in range(n):
    for j in range(n):
        print(f'{a[i][j]:^{WIDTH}g}', end=' ')
    print()

