# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Даны массивы D и F. Сформировать матрицу A по формуле
# $a_{jk}=\sin{(d_j+f_k)}$.
# Определить среднее арифметическое положительных чисел каждой строки матрицы
# и количество элементов, меньших среднего арифметического.
#
# Результаты записать соответственно в массивы AV и L.
# Напечатать матрицу A в виде матрицы и рядом столбцы AV и L.


from math import sin


WIDTH = 11          # output format width
PREC = 5            # output format precision


# Inputs
n_d = int(input("Введите размер массив D: "))     # D size
if n_d < 0:
    print("Размер массив D должен > 0!")
    exit()

n_f = int(input("Введите размер массив F: "))     # F size
if n_f < 0:
    print("Размер массив F должен > 0!")
    exit()

# массив D
print("Введите элемент D массив:")
a_d = [float(input(f"D[{i}]: ")) for i in range(n_d)]

# массив F
print("Введите элемент F массив:")
a_f = [float(input(f"F[{i}]: ")) for i in range(n_f)]

# матрица A
a_a = [[sin(a_d[j]+a_f[k]) for k in range(n_f)] for j in range(n_d)]


# Solve
# массив среднее арифметическое положительных чисел каждой строки матрицы
a_av = []
# массив количество элементов, меньших среднего арифметического
a_l = []


for j in range(n_d):
    sum = 0     # sum positive element
    count = 0   # amount positive element
    for k in range(n_f):
        if a_a[j][k] > 0:
            sum += a_a[j][k]
            count += 1
    if count != 0:
        a_av.append(sum/count)
    else:
        a_av.append(0)
    a_l.append(0)
    for k in range(n_f):
        if a_a[j][k] > 0 and a_a[j][k] < a_av[j]:
            a_l[j] += 1

# Output
print("Матрица:")
print(f"{'A':^{(WIDTH+1)*n_f}}|{'AV':^{WIDTH}}|{'L':^{WIDTH}}")
print(f"{'-'*((WIDTH+1)*n_f+WIDTH+WIDTH)}")
for j in range(n_d):
    for k in range(n_f):
        print(f'{a_a[j][k]:^{WIDTH}.{PREC}g}', end=' ')
    if a_av[j] != 0:
        print(f"|{a_av[j]:^{WIDTH}.{PREC}g}|{a_l[j]:^{WIDTH}.{PREC}g}")
    else:
        print(f"|{'Нет':^{WIDTH}}|{'Нет':^{WIDTH}}")