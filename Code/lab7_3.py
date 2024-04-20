# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вариант п. 1 - 4
# Вариант п. 2 - 2
# Вариант п. 3 - 1
# Вариант п. 4 - 6

# Поиск элемента в списке строк по варианту
#
# Поиск элемента с наибольшим числом английских гласных букв


# Constants
# Гласные буквы английского алфавита
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


# размер списка
n = None
while True:
    n = int(input("Введите размер списка: "))
    if n > 0:
        break
    print("Размер списка должен > 0!")

# список, индекс с нуля
l = [""] * n

# ввод списка
for i in range(n):
    l[i] = str(input(f"Введите {i}-й элемент: "))

# вывод
print("Введенный список: ")
for i in range(n):
    print(f"'{l[i]}'", end=' ')
print()

# Finding
i_max = []          # list index of max vowels string
v_max = 0           # max vowels found
for i in range(n):
    v_cur = 0       # vowels in string
    for j in range(len(l[i])):
        if l[i][j] in VOWELS:
            v_cur += 1

    if v_cur > v_max:
        v_max = v_cur
        i_max = [i]
    elif v_cur == v_max:
        i_max += [i]

# вывод
if v_max:
    print("Элементы с наибольшим числом английских гласных букв:")
    for i in range(len(i_max)):
        print(l[i_max[i]])
else:
    print("Элемент с наибольшим числом английских гласных букв нет.")