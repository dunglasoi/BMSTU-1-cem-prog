# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б

'''Программа позволяет с помощью меню выполнить следующие действия:
1. Выровнять текст по левому краю.
2. Выровнять текст по правому краю.
3. Выровнять текст по ширине.
4. Удаление всех вхождений заданного слова.
5. Замена одного слова другим во всём тексте.
6. Вычисление умножения и деления над целыми числами внутри текста
7. Найти (вывести на экран) и затем самое длинное по количеству предложение'''


# Вычисление самой длинной строки в тексте
def LongestStr(s):
    maxi = len(s[0])
    index = 0
    for i in range(1, len(s)):
        if len(s[i]) > maxi:
            maxi = len(s[i])
            index = i
    return maxi, index


# Вравнивание по левому краю
def Left(s, maxi):
    for i in range(len(s)):
        word = s[i].split()
        x = ''
        for j in range(len(word) - 1):
            x += word[j] + ' '
        x += word[len(word) - 1]
        x += ' ' * (maxi - len(x))
        s[i] = x
    return s


# Вравнивание по правому краю
def Right(s, maxi):
    for i in range(len(s)):
        word = s[i].split()
        x = ''
        for j in range(len(word)):
            if j == len(word) - 1:
                x += word[j]
            else:
                x += word[j] + ' '
        x = ' ' * (maxi - len(x)) + x
        s[i] = x
    return s


# Выравнивание по ширине
def Middle(text, maxi):
    for i in range(len(text) - 1):
        word = text[i].split()
        if len(word) > 1:
            # Находим индексы первого отличного от пробела символа
            j = 0
            while text[i][j] == ' ':
                j += 1
            # Находим индексы последнего отличного от пробела символа
            j1 = len(text[i]) - 1
            while text[i][j1] == ' ':
                j1 -= 1
            text[i] = text[i][j:j1 + 1]
            delta = maxi - len(text[i])  # Разница в длине между текущей строко и максимально длинной строкой
            space = len(word) - 1  # Количество пробелов между словами во всей строке
            x = text[i][0]
            # Распределяем недостоющие пробелы между словами
            if delta % space == 0:
                for m in range(1, len(text[i])):
                    if text[i][m] == ' ' and text[i][m - 1] != ' ':
                        x += text[i][m] + ' ' * (delta // space)
                    else:
                        x += text[i][m]
            else:
                cnt = delta % space
                delta1 = delta // space
                for m in range(1, len(text[i])):
                    if text[i][m] == ' ' and text[i][m - 1] != ' ':
                        if cnt >= 1:
                            x += text[i][m] + ' ' * (delta // space) + ' '
                            cnt -= 1
                        else:
                            x += text[i][m] + ' ' * (delta // space)
                    else:
                        x += text[i][m]
        else:
            x = word[0] + ' ' * (maxi - len(word[0]))  # Если в строке всего одно слово, то добавляем в конец пробелы
        text[i] = x
    j = 0
    # Обрабатываем последнюю строку
    while text[i + 1][j] == ' ':
        j += 1
    text[i + 1] = text[i + 1][j:] + ' ' * (maxi - len(text[i + 1][j:]))
    return text


# Удаление заданного слова
def Delete(s, a):
    # alp = 'ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮюЁё'
    sign = '!@#№$;%^:&?*()_-+=\|/.,<>"{}[]~`'
    exist = False
    for i in range(len(s)):
        x = ''
        x1 = ''
        for j in range(len(s[i])):
            if s[i][j] == ' ' or (s[i][j] in sign):
                if x1 != a:  # Проверяем полученное слово на сходство с заданным
                    x += x1
                    x += s[i][j]
                    x1 = ''
                else:
                    x1 = ''
                    if s[i][j] != ' ':
                        x += s[i][j]
            else:
                x1 += s[i][j]
                if x1 != a and j == len(s[i]) - 1:
                    x += x1
        if s[i] != x:
            exist = True  # Проверка на наличие в тексте заданного слова
        s[i] = x  # Строку текста заменяем на полученную
    if not exist:
        print('\nИскомого слова нет в тексте.', end='\n')
    j = 0
    while j < len(s):
        if len(s[j]) == 0 or (s[j] == ' ' * len(s[j])):
            s.pop(j)
        else:
            j += 1
    return s


# Замена одного слова на другое
def Replace(s, a, change):
    exist = False
    sign = '!@#№$;%^:&?*()_-+=\|/.,<>"{}[]~`'
    for i in range(len(s)):
        x1 = ''
        x = ''
        for j in range(len(s[i])):
            if s[i][j] == ' ' or (s[i][j] in sign):
                if x1 != a:  # Проверяем полученное слово на сходство с заданным
                    x += x1
                    x += s[i][j]
                    x1 = ''
                else:
                    x += change + s[i][j]
                    x1 = ''
            else:
                x1 += s[i][j]
                # Проверяем полученное слово на сходство с заданным
                if x1 != a and j == len(s[i]) - 1:
                    x += x1
                elif x1 == a and j == len(s[i]) - 1:
                    x += change  # Производим замену слова
        if s[i] != x:  # Проверка на наличие в тексте заданного слова
            exist = True
        # Строку текста заменяем на полученную
        s[i] = x
    if not exist:
        print('\nИскомого слова нет в тексте.', end='\n')
    return s


# Составление числа из считанных из строки цифр
def Digits(st, i):
    word = ''
    while i < len(st):
        if not (st[i].isdigit()) or (st[i] == '.'):
            break
        word += st[i]  # Если символ - цифра, то добавляем в строку
        i += 1
    return int(word), i - 1


# Замена символов на их посчитанное выражение
def Change(st, start, p, i):
    st = st[:start] + str(p) + st[i - 1:]
    ind = start + len(str(p)) - 1
    return st, ind


# Вычисление арифметических выражений над целыми числами внутри текста
def Maths(s):
    snew = '\n'.join(s)  # Соеденим все строки в одну
    i = 0
    p, sign, sign2 = None, None, None
    while i < len(snew):
        if snew[i] in '1234567890':
            if p == None:  # Нахождение первого члена выражения
                start = i  # Индекс начала выражения
                p, i = Digits(snew, i)
                if sign != None:
                    start -= 1
                    if sign == '-':
                        p = -p  # Первоначальное значение выражения равно первому числу
                sign, sign2 = None, None
            # Нахождение второго члена выражения
            elif p != None and sign2 != None:
                x, i = Digits(snew, i)
                if sign == '-':
                    x = -x
                if sign2 == '*':  # Вычисление произведения
                    p *= x
                elif sign2 == '/':  # Вычисление частного
                    if x != 0:
                        p //= x
                    else:
                        p = None  # Деление на 0 невозможно
                sign2, sign = None, None
            else:
                snew, i = Change(snew, start, p, i)
                p = None

        elif snew[i] in '-+':
            sign = snew[i]  # Запоминаем знак числа из выражения
        elif snew[i] == ' ':
            if sign != None:
                sign = None

        elif snew[i] in '*/':
            if sign2 != None:
                if p != None:  # Выражение уже имеет значение
                    snew, i = Change(snew, start, p, i)  # Заменяем выражение на его значение
                p, sign2, sign = None, None, None
            else:
                sign2 = snew[i]
        elif snew[i] not in ' \n0123456789*/-+':  # Если встретился знак, который не может быть в выражении
            if p != None:
                snew, i = Change(snew, start, p, i)  # Замена выражения на его значение
            p = None
            sign, sign2 = None, None
        i += 1
    if p != None:
        snew = snew[:start] + str(p)  # Подстановка замененного выражения в строку
    s = snew.split('\n')
    return s


# Поиск самого длинного по количеству слов предложения
def Maxis(s):
    alf = 'ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЁёФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю0123456789'
    maxi = -1
    cnt = 0
    ind11, ind12 = 0, 0
    ind21, ind22 = None, None
    start = False
    sign = '!@#№$;%^:&?*()_-—+=\|/.,<>"{}[]~`'
    x = ''
    for i in range(len(s)):
        new = True
        for j in range(len(s[i])):
            if s[i][j] not in '.!?':
                if not start:
                    ind11 = i  # Начало предложения
                    ind12 = j
                    start = True
                if i > ind11 and new and start:
                    x += ' ' + s[i][j]  # Если преложение занимает несколько строк, то разделяем их пробелами
                    new = False
                else:
                    x += s[i][j]
            elif (j == len(s[i]) - 1 or s[i][j + 1] == ' '):
                x += s[i][j]
                if j < len(s[i]) - 1:
                    x += s[i][j + 1]
                cnt = 0
                if x[0] == ' ':
                    x = x[1:]
                words = x.split()  # Разбиение предложения на слова
                for w in words:
                    if w not in sign:
                        cnt += 1  # Подсчет количества слов
                if cnt > maxi:
                    maxi = cnt
                    # Запоминаем начало и конец искомого предлодения
                    ind11m = ind11
                    ind12m = ind12
                    ind21m = i
                    ind22m = j
                start = False
                x = ''
    x1 = ''
    b = []  # Массив строк без найденного предложения
    # Собираем найденное предложение и массив строк
    for i in range(len(s)):
        if i == ind11m:
            x1 += s[ind11m][ind12m:]
            if len(s[ind11m][:ind12m]) != 0:
                b.append(s[ind11m][:ind12m])
        elif i == ind21m:
            x1 += s[ind21m][:ind22m + 1]
            if len(s[ind21m][ind22m + 1:]) != 0:
                b.append(s[ind21m][ind22m + 1:])
        elif ind11m < i < ind21m:
            x1 += ' ' + s[i]
        else:
            if len(s[i]) != 0:
                b.append(s[i])
    x2 = ''
    cnt = 0
    # Удаляем лишние пробелы между словами в предложении
    for i in range(len(x1)):
        if x1[i] == ' ':
            if cnt < 1:
                cnt += 1
                x2 += x1[i]
        else:
            cnt = 0
            x2 += x1[i]
    return maxi, x2, b


# Исходный текст
text = ["Снимок, сделанный камерой с более чем 1 мегапикселем, ",
        "можно увеличивать до формата примерно 24*30 см, правда, с ",
        "некоторыми оговорками. Разумеется, при этом говорить о ",
        "кадрировании снимка не приходится. В традиционной ",
        "фотографии с негатива размером 24*36 мм можно сделать без ",
        "потери качества отпечаток с увеличением примерно в 10 раз, ",
        "то есть 24*36 см, и качество его будет выше. Резким считается ",
        "отпечаток, имеющий десять линий на миллиметр с пробелами ",
        "такой же ширины, как и линии. С пересчетом на точки при ",
        "равном качестве отпечатков традиционной и цифровой ",
        "фотографий получается, что с негатива размером 24*36 мм ",
        "можно делать увеличения значительно больше, чем в 1000/50 раз."]

# Вывод исходного текста
print('Исходный текст: ')
for i in range(len(text)):
    print(text[i])
print()

# Вывод меню
print('\nМеню: ')
print('1 - Выровнять текст по левому краю.')
print('2 - Выровнять текст по правому краю.')
print('3 - Выровнять текст по ширине.')
print('4 - Удаление всех вхождений заданного слова.')
print('5 - Замена одного слова другим во всем тексте.')
print('6 - Вычисление арифметических выражений над целыми числами.')
print('7 - Найти и затем удалить самое длинное по количеству слов предложение.')
print('0 - Завершения работы меню.')

# Ввод и проверка данных
n = 1
count = 1
while n != 0:
    try:
        if count > 1 and count % 4 == 0:
            print('\nМеню: ')
            print('1 - Выровнять текст по левому краю.')
            print('2 - Выровнять текст по правому краю.')
            print('3 - Выровнять текст по ширине.')
            print('4 - Удаление всех вхождений заданного слова.')
            print('5 - Замена одного слова другим во всем тексте.')
            print('6 - Вычисление арифметических выражений над целыми числами.')
            print('7 - Найти и затем удалить самое длинное по количеству слов предложение.')
            count += 1
            print('0 - Завершения работы меню.')
        ok = True
        n = int(input('\nВведите одну из цифр 1 - 7: '))
        if n == 0:
            print('\nЗавершение работы меню.')
            break
        count += 1
        if (n < 0 or n > 7):
            ok = False
            raise Exception('Введена неверная цифра, попробуйте еще раз')
    except ValueError:
        ok = False
        print('Должна быть введена цифра!')
    except Exception as e:
        ok = False
        print(e)
    if ok:
        # Преобразования текста
        if n == 1:
            maxi = LongestStr(text)[0]
            text = Left(text, maxi)
            print('\nТекст: ')
            for i in range(len(text)):
                print(text[i])
        elif n == 2:
            maxi = LongestStr(text)[0]
            text = Right(text, maxi)
            print('\nТекст: ')
            for i in range(len(text)):
                print(text[i])
        elif n == 3:
            maxi = LongestStr(text)[0]
            text = Middle(text, maxi)
            print('\nТекст: ')
            for i in range(len(text)):
                print(text[i])
        elif n == 4:
            # Ввод и проверка слова для удаления
            while True:
                try:
                    word = input('Введите слово, которое надо удалить: ')
                    if len(word.split()) != 1:
                        raise Exception('Введите одно слово.')
                    else:
                        sign = '!@#№$;%^:&?*()_ -—+=\|/.,<>"{}[]~`'
                        for k in sign:
                            if k in word:
                                raise Exception('Должно быть введено слово или число без знаков.')
                except Exception as e:
                    print(e)
                else:
                    break
            text = Delete(text, word)
            print('\nТекст: ')
            for i in range(len(text)):
                print(text[i])
        elif n == 5:
            # Ввод и проверка слова, которое надо заменить
            while True:
                try:
                    word = input('Введите слово, которое надо заменить: ')
                    if len(word.split()) != 1:
                        raise Exception('Введите одно слово.')
                    else:
                        sign = '!@#№$;%^:&?*()_ -—+=\|/.,<>"{}[]~`'
                        for k in sign:
                            if k in word:
                                raise Exception('Должно быть введено слово, а не знаки препинания.')
                except Exception as e:
                    print(e)
                else:
                    break
            # Ввод слова, которое надо заменить
            word2 = input('Введите слово, на которое надо заменить: ')
            text = Replace(text, word, word2)
            print('\nТекст: ')
            for i in range(len(text)):
                print(text[i])
        elif n == 6:
            text = Maths(text)
            for i in range(len(text)):
                print(text[i])
        elif n == 7:
            length = Maxis(text)[0]
            sent = Maxis(text)[1]
            text = Maxis(text)[2]
            print('\nИскомое предложение длиной {} слов: {}'.format(length, sent))
            print('\nТекст: ')
            if len(text) == 0:
                print('Текст пустой.')
            else:
                for i in range(len(text)):
                    print(text[i])
        elif n == 0:  # Завершение работы меню
            break
        i = 0
        while i < len(text):
            if text[i] == '' or text[i] == ' ' * len(text[i]):
                text.pop(i)
            else:
                i += 1