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

def sx(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

# find
for i in range(n):

