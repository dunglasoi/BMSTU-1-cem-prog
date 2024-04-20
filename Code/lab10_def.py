PREC = 5
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


def rectangle_middle_method(f, a, b, n):
    """Метод средних прямоугольников

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
    # half inteval
    h_half = h/2

    # sum
    sum = 0
    x = a+h
    for _ in range(1, n+1):
        print(x-h_half)
        sum += f(x - h_half)
        x += h

    # integral
    return h * sum


def fun_dx(x):
    """Интегрируемая функция"""
    return 2*x
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
    n = input_int("количество участков разбиения N")
    if n > 0:
        break
    print("Количество участков разбиения N должно > 0!")
i = rectangle_middle_method(fun_dx, a, b, n)
print(f"{i:.{PREC}}")