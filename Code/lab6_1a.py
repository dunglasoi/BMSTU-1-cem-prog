# Программа сделана Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Вариант п. 4 - 4
# Вариант п. 5 - 3
# Добавить элемент в заданное место списка (по индексу) с использованием любых средств Python

n = None
while True:
    n = int(input("Введите размер списка: "))
    if n > 0:
        break
    print("Размер списка должен > 0!")

l = list()
l = [0] * n

for i in range(n):
    l[i] = int(input(f"Введите {i}-й элемент: "))

while True:
    print("Вывод списка: ")
    for i in range(n):
        print(l[i], end='  ')

    if n <= 0:
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
        print(f"Индекс вне диапазона! Индекс должен быть в диапазоне: [0;{n}]")

    # элемент
    elm = int(input("Введите {idx}-й элемент: "))

    # условие выхода
    if not elm:
        break

    #вставлять
    l += [0]
    n += 1
    l.insert(idx, elm)