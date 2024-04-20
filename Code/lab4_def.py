from math import cos

st = float(input("Введите начало: "))
step = float(input("Введите шаг: "))
en = float(input("Введите конец: "))
x1 = st
min_y = cos(st) - 1
max_y = cos(st) - 1
while x1 <= en:
    y = cos(x1) - 1
    if y >= max_y:
        max_y = y
    if y <= min_y:
        min_y = y
    x1 += step
i = 0
print(' ' * 7, end='')
print(f"{min_y:.3g}".ljust(84) + f"{max_y:.3g}")
x2 = st
while x2 <= en:
    y = cos(x2) - 1
    len_result = int((y - min_y) * (84 / abs(max_y - min_y)))
    zero = int(abs(min_y) * (84 / abs(max_y - min_y)))
    if min_y >= 0:
        print(f'{x2:.6g}'.ljust(6) + '|' + str('*').rjust(len_result))
    elif min_y < 0 and max_y > 0:
        if y < 0:
            if len_result == 0:
                if zero - len_result <= 1:
                    print(f'{x2:.6g}'.ljust(6) + '|' + '*'.rjust(len_result))
                else:
                    print(f'{x2:.6g}'.ljust(6) + '|' + '*'.rjust(len_result) +
                      '|'.rjust(zero - len_result-1))
            else:
                if zero - len_result < 1:
                    print(f'{x2:.6g}'.ljust(6) + '|' + '*'.rjust(len_result))
                else:
                    print(f'{x2:.6g}'.ljust(6) + '|' + '*'.rjust(len_result) +
                      '|'.rjust(zero - len_result))

        elif abs(y-0) < 0.1:
            print(f'{x2:.6g}'.ljust(6) + '|' + '*'.rjust(zero))
        else:
            print(f'{x2:.6g}'.ljust(6) + '|' + '|'.rjust(zero) + '*'.rjust(len_result-zero))
    else:
        print(f'{x2:.6g}'.ljust(6) + '|' + str('*').rjust(len_result))
    x2 += step
    if (abs(x2)) < 1e-5:
        x2 = 0
