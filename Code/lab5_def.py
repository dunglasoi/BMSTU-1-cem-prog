from math import factorial

WIDTH = 11
PREC = 5

x = None
eps = None
max_iter = None
print_step = None

x = float(input('Введите значение переменой x: '))
while round(x, 3) == 0:
    x = float(input('Введите значение переменой x снова: '))

while True:
    eps = float(input("Введите точность: "))
    if eps <= 0:
        print("Точность должна > 0!")
        continue
    break

while True:
    max_iter = int(input("Введите максимальное количество итераций: "))
    if max_iter < 1:
        print("Максимальное количество итераций должно > 0!")
        continue
    break

while True:
    print_step = int(input("Введите шаг печати: "))
    if print_step < 1:
        print("Шаг печати должен > 0!")
        continue
    break

i = 1
s = 1
y = i * x / factorial(i)

if y > eps:
    print(f"{'':-^43}")
    print("|   {:^{w}}| {:^{w}}|  {:^{w}}|"
          .format('№ итерации', 'y', 's', w=WIDTH))
    print(f"|{'':-^42}")

while y > eps:

    y = i * x / factorial(i)
    s += y

    if i % print_step == 1 or print_step == 1:
        print("|   {:<{w}.{p}g}| {:<{w}.{p}g}|  {:<{w}.{p}g}|"
              .format(i, y, s, w=WIDTH, p=PREC))

    i += 1

    if i > max_iter:
        print(f"{'':-^43}")
        print("За указанное число итераций необходимой "
              "точности достичь не удалось")
        break

if i <= max_iter:
    if i > 1:
        print(f"{'':-^43}")
    print(f"Сумма бесконечного ряда - {s:.{PREC}g},"
          f" вычислена за {i} итераций.")