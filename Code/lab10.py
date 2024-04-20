# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Вычисление приближённого значения интеграла
# Метод 1: правых прямоугольников
# Метод 2: трапеций


# Constants
WIDTH = 15          # output format width
PREC = 5            # output format precision


# Input function with validation
def input_int(msg):
    """Input int number"""
    while True:
        try:
            x = int(input(f"Введите {msg}: "))
            break
        except Exception:
            print(f"{msg} must be int number!")
    return x


def input_float(msg):
    """Input float number"""
    while True:
        try:
            x = float(input(f"Введите {msg}: "))
            break
        except Exception:
            print(f"{msg} must be float number!")
    return x


# Численное интегрирование методы
def rectangle_right_method(f, a, b, n):
    """Метод правых прямоугольников

    Parameters
    ----------
    f : function
        Функция интегрирование
    a : float
        Начало отрезка интегрирования
    b : float
        Конец отрезка интегрирования
    n : int
        Количество участков разбиения

    Returns
    -------
    integral : float
        Значение интеграла
    """
    # inteval size
    h = (b-a)/n

    # sum
    sum = 0
    x = a+h
    for _ in range(1, n+1):
        sum += f(x)
        x += h

    # integral
    return h * sum




def trapezoid_method(f, a, b, n):
    """Метод трапеций

    Parameters
    ----------
    f : function
        Функция интегрирование
    a : float
        Начало отрезка интегрирования
    b : float
        Конец отрезка интегрирования
    n : int
        Количество участков разбиения

    Returns
    -------
    integral : float
        Значение интеграла
    """
    # inteval size
    h = (b-a)/n

    # sum
    sum = 0
    x = a+h
    for _ in range(1, n):
        sum += f(x)
        x += h

    # integral
    return h/2 * (f(a) + f(b) + 2*sum)


def integral(f, a, b):
    """Точное значение интеграла"""
    return f(b) - f(a)


# Интегрируемая функция
def fun_dx(x):
    """Интегрируемая функция"""
    return x*x#2*x


# Первообразная функция
def fun(x):
    """Первообразная функция"""
    return 2*x#x**2


# Inputs
while True:
    # начало отрезка интегрирования
    a = input_float("начало отрезка интегрирования")
    # конец отрезка интегрирования
    b = input_float("конец отрезка интегрирования")
    if b >= a:
        break
    print("Конец отрезка интегрирования должен >= начало!")

while True:
    # количество участков разбиения N1
    n1 = input_int("количество участков разбиения N1")
    if n1 > 0:
        break
    print("Количество участков разбиения N1 должно > 0!")

while True:
    # количество участков разбиения N2
    n2 = input_int("количество участков разбиения N2")
    if n2 > 0:
        break
    print("Количество участков разбиения N2 должно > 0!")

print()

# calculate ~ integral
i1 = rectangle_right_method(fun_dx, a, b, n1)
i2 = rectangle_right_method(fun_dx, a, b, n2)
i3 = trapezoid_method(fun_dx, a, b, n1)
i4 = trapezoid_method(fun_dx, a, b, n2)

# output table
print(f"{'-'*(WIDTH*3+4)}")
print(f"|{'':^{WIDTH}}|{'N1':^{WIDTH}}|{'N2':^{WIDTH}}|")
print(f"{'-'*(WIDTH*3+4)}")

print(f"|{'Метод 1':<{WIDTH}}|{i1:^{WIDTH}.{PREC}}|{i2:^{WIDTH}.{PREC}}|")
print(f"|{'Метод 2':<{WIDTH}}|{i3:^{WIDTH}.{PREC}}|{i4:^{WIDTH}.{PREC}}|")
print(f"{'-'*(WIDTH*3+4)}")

print()

# exact integral
i_exact = integral(fun, a, b)
print(f"Точное значение интеграла: {i_exact:{WIDTH}.{PREC}}")
print()

# абсолютная погрешность
error1 = abs(i1-i_exact)
error2 = abs(i2-i_exact)
error3 = abs(i3-i_exact)
error4 = abs(i4-i_exact)

print(f"Абсолютная погрешность метод 1 при N1: {error1:{WIDTH}.{PREC}}")
print(f"Абсолютная погрешность метод 1 при N2: {error2:{WIDTH}.{PREC}}")
print(f"Абсолютная погрешность метод 2 при N1: {error3:{WIDTH}.{PREC}}")
print(f"Абсолютная погрешность метод 2 при N2: {error4:{WIDTH}.{PREC}}")

print()

# относительная погрешность
error1p = abs(error1/i_exact)
error2p = abs(error2/i_exact)
error3p = abs(error3/i_exact)
error4p = abs(error4/i_exact)

print(f"Относительная погрешность метод 1 при N1: {error1p:{WIDTH}.{PREC}}")
print(f"Относительная погрешность метод 1 при N2: {error2p:{WIDTH}.{PREC}}")
print(f"Относительная погрешность метод 2 при N1: {error3p:{WIDTH}.{PREC}}")
print(f"Относительная погрешность метод 2 при N2: {error4p:{WIDTH}.{PREC}}")

print()


while True:
    # точность эпсилон
    eps = input_float("точность eps")
    if eps > 0:
        break
    print("Точность eps должна > 0!")

# list error
l_error = [error1, error2, error3, error4]
idx_max_error = l_error.index(max(l_error))
# less accurate method
g = rectangle_right_method if idx_max_error < 2 else trapezoid_method

# количество участков разбиения,
# для которого интеграл будет вычислен с заданной точностью
n = 1
if g == rectangle_right_method:
    n = 1
if g == trapezoid_method:
    n = 2
g1 = g(fun_dx, a, b, n)
g2 = g(fun_dx, a, b, 2*n)
while abs((g1 - g2)) >= eps:
    g1 = g2
    n *= 2
    g2 = g(fun_dx, a, b, 2*n)

print("Количество участков разбиения, для которого интеграл будет вычислен\n"
      f"с заданной точностью: {n}")
print(g2)
