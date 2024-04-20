# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б

n = None
while True:
    n = int(input("Введите размер массив: "))
    if n > 0:
        break
    print("Размер списка должен > 0!")

# список, индекс с нуля
l = list()
l = [0] * n

for i in range(n):
    l[i] = int(input(f"Введите {i}-й элемент: "))

# добавление
print("Вывод массив: ")
for i in range(n):
        print(l[i], end='  ')

zero = [i for i in l if i != 0]
print("\nНовый массив: ", zero)