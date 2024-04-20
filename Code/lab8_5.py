# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 3 - 2

# Найти максимальное значение в квадратной матрице над главной диагональю
# и минимальное - под побочной диагональю.


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
print("Введенная матрица:")
for i in range(n):
    for j in range(n):
        print("{:^5g}".format(a[i][j]), end=' ')
    print()


#
# Главная диагональ: элементы из левого верхнего угла в правый нижний угол
# Побочная диагональ: элементы из левого нижнего угла в правый верхний угол
#

# find
min = None     # min element
max = None     # max element

for i in range(n):
    for j in range(i+1, n):
        if max == None or a[i][j] > max:
            max = a[i][j]
        if min == None or a[n-1-i][j] < min:
            min = a[n-1-i][j]


# Output
if max != None:
    print(f"Максимальное значение: {max}")
else:
    print(f"Максимальное значение нет")
if min != None:
    print(f"Минимальное значение: {min}")
else:
    print(f"Минимальное значение нет")