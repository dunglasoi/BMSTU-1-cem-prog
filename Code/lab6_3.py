# Программа сделана Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Вариант п. 4 - 4
# Вариант п. 5 - 3
# Найти значение K-го экстремума в списке


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

# k extremum
k = None
while True:
    k = int(input("Введите K-го экстремума: "))
    if k > 0:
        break
    print("K-ый экстремум должен > 0!")

# k extremum
k_etr = None
# найти
i = 1
while k > 0 and i < n-1:
    if l[i-1] < l[i] > l[i+1] or l[i-1] > l[i] < l[i+1]:
        k_etr = l[i]
        k -= 1
    i += 1

# найти или нет
if k_etr is not None and k == 0:
    print(f"Значение K-го экстремума: {k_etr}")
else:
    print("Значение K-го экстремума не найдено.")

