# Программа сделана Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Вариант п. 4 - 4
# Вариант п. 5 - 3
# Добавить элемент в заданное место списка (по индексу) алгоритмически.


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

# Добавление
while True:
    # вывод измененного списка
    print("Вывод списка: ")
    for i in range(n):
        print(l[i], end=' ')

    if n <=0:
        print()
        break
    print("\nДля завершения введите индекс -1")

        # индекс, куда вставить
    idx = None
    while True:
        idx = int(input("Введите индекс: "))
        if idx == -1:
            exit()
        if 0 <= idx <= n:
            break
        print(f'Индекс вне диапазона! Индекс должен быть в диапазоне: [0;{n}]')

    # элемент для вставки
    elm = input(f"Введите {id}-й элемент: ")

    # exit condition
    if not elm:
        break

    # вставки
    l += [0]
    n += 1
    for i in range(n-1, idx, -1):
        l[i] = l[i-1]
    l[idx] = int(elm)

