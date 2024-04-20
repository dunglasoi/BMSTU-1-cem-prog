# Программа сделана Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Вариант п. 4 - 4
# Вариант п. 5 - 3
# Поменять местами элементы с характеристиками по варианту.
# Минимальный положительный и максимальный положительный.

# размер списка
n = None
while True:
    n = int(input("Введите размер списка: "))
    if n > 0:
        break
    print("Размер списка должен > 0!")

# список, индекс с нуля
l = list()
l = [0] * n

# ввод списка
for i in range(n):
    l[i] = int(input(f"Введите {i}-й элемент: "))

# вывод списка
print("Вывод списка: ")
for i in range(n):
    print(l[i], end=' ')
print()

# найти минимальный положительный элемент и максимальный положительный элемент
idx_min_pos = -1         # индекс минимальный положительный элемент
idx_max_pos = -1         # индекс максимальный положительный элемент
for i in range(n):
    if l[i] <= 0:
        continue
    if idx_max_pos == -1 or 0 < l[i] > l[idx_max_pos]:
        idx_max_pos = i
    if idx_min_pos == -1 or 0 < l[i] < l[idx_min_pos]:
        idx_min_pos = i

# изменить свою позицию
if idx_min_pos > -1 and idx_max_pos > -1:
    l[idx_min_pos], l[idx_max_pos] = l[idx_max_pos], l[idx_min_pos]

# вывод списка
print("Вывод списка: ")
for i in range(n):
    print(l[i], end=' ')
print()