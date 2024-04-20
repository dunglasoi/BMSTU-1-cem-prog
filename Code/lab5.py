# Программа сделана Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Вычислить сумму ряда с заданной точностью и вывести таблицу промежуточних значений c заданным шагом.
# Ряд: 1 / ((n + 1) ** 2 - 1)

# Constants
WIDTH = 11          # format width
PREC = 5            # format precision


# Inputs
eps = None                  # точность
max_iter = None             # максимальное количество итераций
print_step = None           # шаг печати

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


# Таблица
i = 1                       # n - аргумент
s = 0                       # y - сумма
y = 1 / ((i + 1) ** 2 - 1)  # значение текущего члена

# table header
if y > eps:
    print(f"{'':-^43}")
    print("|   {:^{w}}| {:^{w}}|  {:^{w}}|"
          .format('№ итерации', 'y', 's', w=WIDTH))
    print(f"|{'':-^42}")

while y > eps:

    y = 1 / ((i + 1) ** 2 - 1)
    s += y

    # вывод значения таблицы
    if i % print_step == 1 or print_step == 1:
        print("|   {:<{w}.{p}g}| {:<{w}.{p}g}|  {:<{w}.{p}g}|"
              .format(i, y, s, w=WIDTH, p=PREC))

    i += 1

    # превысили максимальной итерации
    if i > max_iter:
        print(f"{'':-^43}")
        print("За указанное число итераций необходимой "
              "точности достичь не удалось")
        break

# вывод результата
if i <= max_iter:
    if i > 1:
        print(f"{'':-^43}")
    print(f"Сумма бесконечного ряда - {s:.{PREC}g},"
          f" вычислена за {i} итераций.")