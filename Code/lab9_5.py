# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на точки.
# Напечатать матрицу до и после преобразования.


# Гласные буквы английского алфавита
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


# Inputs
row_d = int(input("Введите количество строк матрицы: "))        # matrix D rows
if row_d < 0:
    print("Количество строк матрицы должно > 0!")
    exit()

col_d = int(input("Введите количество столбцов матрицы: "))     # matrix D columns
if col_d < 0:
    print("Количество столбцов матрицы должно > 0!")
    exit()

# matrix D
print("Введите элемент матрицы:")
a_d = [[input(f"D[{i}][{j}]: ") for j in range(col_d)]
       for i in range(row_d)]

# output D pre transformation
print("Матрица до преобразования:")
for i in range(row_d):
    for j in range(col_d):
        print(f'{a_d[i][j]}', end=' ')
    print()

# transform
for i in range(row_d):
    for j in range(col_d):
        if a_d[i][j] in VOWELS:
            a_d[i][j] = '.'

# output D after transformation
print("Матрица после преобразования:")
for i in range(row_d):
    for j in range(col_d):
        print(f'{a_d[i][j]}', end=' ')
    print()