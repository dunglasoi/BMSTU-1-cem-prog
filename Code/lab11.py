# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Исследование методов сортировки
# метод Шелла

# Constants
WIDTH = 12
PREC = 5
EPS = 1e-9

from random import randint
from time import time


# метод Шелла
def shell_sort(data):
    """Метод Шелла"""
    start_time = time()  # время начала выполнения
    swap_time = 0  # поменять время

    n = len(data)
    step = n // 2
    while step > 0:
        for i in range(step, n, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                swap_time += 1
                j = delta
                delta = j - step
        step //= 2

    end_time = time()  # время окончания выполнения
    return end_time - start_time, swap_time


def random_ints(n):
    """Return list[n] random int"""
    a = [randint(0, 1000) for i in range(n)]
    return a


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


def float_to_str(x):
    if x == None:
        return f"{'нет':^{WIDTH}}"
    elif abs(x) < EPS:
        return f"{0.0:^{WIDTH}}"
    else:
        return f"{x:^{WIDTH}.{PREC}}"


def int_to_str(x):
    return f"{x:^{WIDTH}}"


def print_array_int(data, msg):
    print(f"{msg}:")
    for i in range(len(data)):
        print(f'{data[i]}', end=' ')
    print()


# part 1
# Inputs
while True:
    # array size
    n = input_int("размер массива")
    if n > 0:
        break
    print("Размер массива должен > 0!")

# array A
a = [input_int(f'A[{i}] ') for i in range(n)]

print()

# output A
print_array_int(a, 'Array A')
print()

# sort
shell_sort(a)

# output A
print_array_int(a, 'Array A after sort')
print()

# part 2
# array size
while True:
    # array size
    n1 = input_int("размер массива N1")
    if n1 > 0:
        break
    print("Размер массива N1 должен > 0!")

while True:
    # array size
    n2 = input_int("размер массива N2")
    if n2 > 0:
        break
    print("Размер массива N2 должен > 0!")

while True:
    # array size
    n3 = input_int("размер массива N3")
    if n3 > 0:
        break
    print("Размер массива N3 должен > 0!")

print()

# array random ints
a1 = random_ints(n1)
a2 = random_ints(n2)
a3 = random_ints(n3)

# array sorted
a1_sort = a1.copy()
a2_sort = a2.copy()
a3_sort = a3.copy()
a1_sort.sort()
a2_sort.sort()
a3_sort.sort()

# array sorted reverse
a1_sort_rev = a1.copy()
a2_sort_rev = a2.copy()
a3_sort_rev = a3.copy()
a1_sort_rev.sort(reverse=True)
a2_sort_rev.sort(reverse=True)
a3_sort_rev.sort(reverse=True)


# time, count permutation
t1, k1 = shell_sort(a1_sort)
t2, k2 = shell_sort(a2_sort)
t3, k3 = shell_sort(a3_sort)
t4, k4 = shell_sort(a1)
t5, k5 = shell_sort(a2)
t6, k6 = shell_sort(a3)
t7, k7 = shell_sort(a1_sort_rev)
t8, k8 = shell_sort(a2_sort_rev)
t9, k9 = shell_sort(a3_sort_rev)

# table
print(f"{' ':{33}}|{'N1':^{WIDTH * 2 + 1}}|{'N2':^{WIDTH * 2 + 1}}|{'N3':^{WIDTH * 2 + 1}}")
print("{1}|{0}|{0}|{0}"
      .format(f"{'время(c)':^{WIDTH}}|{'перестановки':^{WIDTH}}", f"{' ':{33}}"))
print(f"{'Упорядоченный список':{33}}|"
      f"{float_to_str(t1)}|{int_to_str(k1)}|"
      f"{float_to_str(t2)}|{int_to_str(k2)}|"
      f"{float_to_str(t3)}|{int_to_str(k3)}")
print(f"{'Случайный список':{33}}|"
      f"{float_to_str(t4)}|{int_to_str(k4)}|"
      f"{float_to_str(t5)}|{int_to_str(k5)}|"
      f"{float_to_str(t6)}|{int_to_str(k6)}")
print(f"{'Упорядоченный в обратном порядке':{33}}|"
      f"{float_to_str(t7)}|{int_to_str(k7)}|"
      f"{float_to_str(t8)}|{int_to_str(k8)}|"
      f"{float_to_str(t9)}|{int_to_str(k9)}")