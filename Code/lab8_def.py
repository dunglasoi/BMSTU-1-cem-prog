m = int(input("Введите количество строк матрицы: "))
if m < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

n = int(input("Введите количество столбцов матрицы: "))
if n < 0:
    print("Количество столбцов матрицы должно > 0!")
    exit()

a = [[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input(f'Введите элемент A[{i}][{j}]: '))

print("Введенная матрица: ")
for i in range(m):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()

cur = 0
c = 0
for i in range(m):
    cur = 0
    for j in range(n):
        if a[i][j] != 0:
            cur += 1
    if cur == n:
        for d in range(n):
            a[c][d] = a[i][d]
        c += 1

print("Новая матрица:")
for i in range(m-c):
    a.pop()
for i in range(len(a)):
    for j in range(len(a[i])-1):
        print("{:^5g}".format(a[i][j]), end='')
    print("{:^5g}".format(a[i][len(a[i])-1]))







