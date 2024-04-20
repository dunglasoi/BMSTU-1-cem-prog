# Программа сделана Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Вариант п. 4 - 4
# Вариант п. 5 - 3
# Удалить элемент с заданным индексом алгоритмически

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

for i in range(n):
    l[i] = int(input(f"Введите {i}-й элемент: "))

# добавление
while True:
    print("Вывод списка: ")
    for i in range(n):
        print(l[i], end='  ')

    if n <= 0:
        print()
        break
    print("\nДля завершения введите индекс -1")

# вставлять
    idx = None
    while True:
        idx = int(input("Введите индекс: "))
        if idx == -1:
            exit()
        if 0 <= idx < n:
            break
        print(f'Индекс вне диапазона! Индекс должен быть в диапазоне: [0;{n-1}]')

# Удалить
    for i in range(idx + 1, n):
        l[i-1] = l[i]
    del l[-1]
    n -= 1
