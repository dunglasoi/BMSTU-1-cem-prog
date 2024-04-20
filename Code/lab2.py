# Нгуен Ань Зунг
# Группа ИУ7И-11Б
# Блок-схема y = ax^2 + bx + c

import math as m

a = float(input("Введите a: "))  #Ввод значение a
b = float(input("Введите b: "))  #Ввод значение b
c = float(input("Введите c: "))  #Ввод значение c

if a == 0:                       # a == 0 уравнение становится уравнением первой степени bx + c = 0
    if b == 0:
        if c == 0:
            print("x - Любое")
        else:
            print("Нет решения")
    else:
        x = -c / b
        print('x = {:5g}'.format(x))
else:
    delta = pow(b, 2) - 4 * a * c                       #считать дискриминации
    if delta > 0:
        x1 = (-b + m.sqrt(delta)) / (2 * a)
        print('x1 = {:5g}'.format(x1))                  #Вывод значение x1
        x2 = (-b - m.sqrt(delta)) / (2 * a)
        print('x2 = {:5g}'.format(x2))                  #Вывод значение x2
    else:
        delta == 0
        if delta == 0:
            x = -b / (2 * a)
            print('x = {:5g}'.format(x))                #Вывод значение x
        else:
            print("Нет решения")






