# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# Метод расчёски

def print_array_int(data, msg):
    print(f"{msg}:")
    for i in range(len(data)):
        print(f'{data[i]}', end=' ')
    print()

# метод расчёски
def comb_sort(data):
    """Метод расчёски"""
    factor = 1.247330950103979

    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / factor))  # minimum gap is 1
        swaps = False
        for i in range(len(data) - gap):
            j = i+gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True
    return data


# array size
n = int(input("n: "))

# array A
a = [int(input(f'A[{i}]: ')) for i in range(n)]

# output A
print_array_int(a, 'Array A')
print()

# sort
a = comb_sort(a)

# output A
print_array_int(a, 'Array A after sort')
print()


