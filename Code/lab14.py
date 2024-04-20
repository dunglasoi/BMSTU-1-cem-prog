# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
# База данных в бинарном файле

import struct
from struct import pack, unpack
import os

def input_int(msg):
    while True:
        try:
            x = int(input(f"Введите {msg}: "))
            break
        except Exception:
            print(f"{msg} должен быть int число!")
    return x


def input_float(msg):
    while True:
        try:
            x = float(input(f"Введите {msg}: "))
            break
        except Exception:
            print(f"{msg} должен быть float число!")
    return x

# column name
COL_NAME = ('Name', 'Age', 'Point')
# string width
STR_WIDTH = 20
# struct format
COL_FORMAT = f'{STR_WIDTH}sif'
# max string length
STR_LEN = 50
# string encoding
ENCODING = 'utf-8'


def str_pack(s):
    return bytes(s, ENCODING)


def str_unpack(s):
    return s.decode().replace('\x00', '')


def is_db_empty(fd):
    fd.seek(0)
    size = struct.calcsize(COL_FORMAT)
    while fd.read(size):
        return False
    return True


def count_record(fd):
    fd.seek(0)
    i = 0
    size = struct.calcsize(COL_FORMAT)
    while fd.read(size):
        i += 1
    return i


def open_db():
    """Open db"""
    while True:
        try:
            print('Выберите файл для работы:')
            filename = input('> ')

            # create file if not exist
            if not os.path.exists(filename):
                fd = open(filename, 'w+')
                fd.close()

            fd = open(filename, 'r+b')

            # check db integrity
            fd.seek(0)
            size = struct.calcsize(COL_FORMAT)
            while line := fd.read(size):
             _ = unpack(COL_FORMAT, line)

            return fd

        except struct.error as e:
            print('Database is corrupted!')

        except Exception as e:
            print(e)


def init_db(fd):
    """Initialize db"""
    # check access
    if not os.access(fd.name, os.W_OK):
        print("File has no write access!")
        return

    # delete file content
    fd.truncate(0)

    # insert records
    fd.seek(0)
    fd.write(pack(COL_FORMAT, str_pack('ABC'), 18, 95))
    fd.write(pack(COL_FORMAT, str_pack('BCD'), 17, 72))
    fd.write(pack(COL_FORMAT, str_pack('ACD'), 20, 100))


def output_db(fd):
    """Output all record from db"""
    # check access
    if not os.access(fd.name, os.R_OK):
        print("File has no read access!")
        return

    if is_db_empty(fd):
        print("Database is empty!")
        print()
        return

    width = [STR_WIDTH, 11, 11]

    # output column name
    print(f"{'':3}", end='')
    print(
        f"| {COL_NAME[0]:^{width[0]}}|{COL_NAME[1]:^{width[1]}}|{COL_NAME[2]:^{width[2]}}")
    # output records
    fd.seek(0)
    c = 0
    size = struct.calcsize(COL_FORMAT)
    while line := fd.read(size):
        l = unpack(COL_FORMAT, line)
        c += 1
        print(f"{c:3}", end='')
        print(f"| {str_unpack(l[0]):{width[0]}}", end='')
        print(f"|{l[1]:^{width[1]}}", end='')
        print(f"|{l[2]:^{width[2]}.5g}", end='')
        print()
    print()


def insert_db(fd):
    """Insert 1 record into db"""
    # check access
    if not os.access(fd.name, os.W_OK):
        print("File has no write access!")
        return

    total = count_record(fd)
    size = struct.calcsize(COL_FORMAT)

    try:
        idx = input_int("Index to insert: ")
        if not (1 <= idx <= total + 1):
            raise Exception(f'Index: must be in [1;{total + 1}].')
        name = input('Name: ')
        if len(name) > STR_WIDTH:
            raise Exception('Name: string too long.')
        age = input_int('Age: ')
        if age < 6:
            raise Exception('Age: too young.')
        if age > 100:
            raise Exception('Age: too old.')
        point = input_float('Point: ')
        if not (0 <= point <= 100):
            raise Exception('Point: must be in [0; 100].')

        # move record to end
        fd.seek(0, os.SEEK_END)
        i = total - idx + 1
        while i > 0:
            fd.seek(-size, os.SEEK_CUR)
            rec = fd.read(size)
            fd.write(rec)
            fd.seek(-2 * size, os.SEEK_CUR)
            i -= 1

        # insert records
        fd.seek((idx - 1) * size)
        fd.write(pack(COL_FORMAT, str_pack(name), age, point))

        print()

    except Exception as e:
        print("Insertion failed!")
        print(e)


def delete_db(fd):
    """Delete 1 record from db"""
    if not os.access(fd.name, os.W_OK):
        print("File has no write access!")
        return

    if is_db_empty(fd):
        print("Database is empty!")
        print()
        return

    total = count_record(fd)
    size = struct.calcsize(COL_FORMAT)
    try:
        idx = input_int("Index to delete: ")
        if not (1 <= idx <= total):
            raise Exception(f'Index: must be in [1;{total}].')

        # delete: move record 1 position to start
        fd.seek((idx) * size)
        i = idx
        while i < total:
            rec = fd.read(size)
            t = fd.tell()
            fd.seek(-2 * size, os.SEEK_CUR)
            t = fd.tell()
            fd.write(rec)
            t = fd.tell()
            fd.seek(size, os.SEEK_CUR)
            t = fd.tell()
            i += 1

        # delete last record
        fd.truncate((total - 1) * size)

        print("Удаление получилость")
        print()

    except Exception as e:
        print("Deletion failed!")
        print(e)


def find_1_db(fd):
    """Поиск по одному полю"""
    # check access
    if not os.access(fd.name, os.R_OK):
        print("File has no read access!")
        return

    if is_db_empty(fd):
        print("Database is empty!")
        print()
        return

    width = [STR_WIDTH, 11, 11]
    size = struct.calcsize(COL_FORMAT)

    try:
        print("Доступные поля:")
        for i in range(len(COL_NAME)):
            print(f"{i}. {COL_NAME[i]}")
        idx = input_int("Выберите поле> ")
        if not (0 <= idx < len(COL_NAME)):
            raise Exception('Некорректное поле!')

        word = None
        if idx == 0:
            s = input('Ключевое слово: ')
            if len(s) > STR_WIDTH:
                raise Exception('Name: string too long.')
            word = pack(COL_FORMAT, str_pack(s), 0, 0)
        elif idx == 1:
            s = input_int('Ключевое слово: ')
            word = pack(COL_FORMAT, b'\x00', s, 0)
        elif idx == 2:
            s = input_float('Ключевое слово: ')
            word = pack(COL_FORMAT, b'\x00', 0, s)

        word = unpack(COL_FORMAT, word)

        fd.seek(0)
        c = 0
        r = 0
        while line := fd.read(size):
            c += 1
            l = unpack(COL_FORMAT, line)
            if l[idx] == word[idx]:
                r += 1
                if r == 1:
                    # output column name
                    print(f"{'':3}", end='')
                    print(
                        f"| {COL_NAME[0]:^{width[0]}}|{COL_NAME[1]:^{width[1]}}|{COL_NAME[2]:^{width[2]}}")

                # output found record
                print(f"{c:3}", end='')
                print(f"| {str_unpack(l[0]):{width[0]}}", end='')
                print(f"|{l[1]:^{width[1]}}", end='')
                print(f"|{l[2]:^{width[2]}.5g}", end='')
                print()

        if r == 0:
            print('Нет совпадение!')
        print()

    except Exception as e:
        print(e)
        print()


def find_2_db(fd):
    """Поиск по двум полям"""
    # check access
    if not os.access(fd.name, os.R_OK):
        print("File has no read access!")
        return

    if is_db_empty(fd):
        print("Database is empty!")
        print()
        return

    width = [STR_WIDTH, 11, 11]
    size = struct.calcsize(COL_FORMAT)

    try:
        print("Доступные поля:")
        for i in range(len(COL_NAME)):
            print(f"{i}. {COL_NAME[i]}")

        # field 1
        idx = input_int("Выберите поле 1> ")
        if not (0 <= idx < len(COL_NAME)):
            raise Exception('Некорректное поле!')

        word = None
        if idx == 0:
            s = input('Ключевое слово 1: ')
            if len(s) > STR_WIDTH:
                raise Exception('Name: string too long.')
            word = pack(COL_FORMAT, str_pack(s), 0, 0)
        elif idx == 1:
            s = input_int('Ключевое слово 1: ')
            word = pack(COL_FORMAT, b'\x00', s, 0)
        elif idx == 2:
            s = input_float('Ключевое слово 1: ')
            word = pack(COL_FORMAT, b'\x00', 0, s)

        word1 = unpack(COL_FORMAT, word)
        idx1 = idx

        # field 2
        idx = input_int("Выберите поле 2> ")
        if not (0 <= idx < len(COL_NAME)):
            raise Exception('Некорректное поле!')

        word = None
        if idx == 0:
            s = input('Ключевое слово 2: ')
            if len(s) > STR_WIDTH:
                raise Exception('Name: string too long.')
            word = pack(COL_FORMAT, str_pack(s), 0, 0)
        elif idx == 1:
            s = input_int('Ключевое слово 2: ')
            word = pack(COL_FORMAT, b'\x00', s, 0)
        elif idx == 2:
            s = input_float('Ключевое слово 2: ')
            word = pack(COL_FORMAT, b'\x00', 0, s)

        word2 = unpack(COL_FORMAT, word)
        idx2 = idx

        del word
        del idx

        if idx1 == idx2:
            raise Exception('Одинаковые поля!')

        fd.seek(0)
        c = 0
        r = 0
        while line := fd.read(size):
            c += 1
            l = unpack(COL_FORMAT, line)
            if l[idx1] == word1[idx1] and l[idx2] == word2[idx2]:
                r += 1
                if r == 1:
                    # output column name
                    print(f"{'':3}", end='')
                    print(
                        f"| {COL_NAME[0]:^{width[0]}}|{COL_NAME[1]:^{width[1]}}|{COL_NAME[2]:^{width[2]}}")

                # output found record
                print(f"{c:3}", end='')
                print(f"| {str_unpack(l[0]):{width[0]}}", end='')
                print(f"|{l[1]:^{width[1]}}", end='')
                print(f"|{l[2]:^{width[2]}.5g}", end='')
                print()

        if r == 0:
            print('Нет совпадение!')
        print()

    except Exception as e:
        print(e)
        print()


def menu(fd):
    """Menu"""
    # print options
    print(
        "Выберите действие:\n"
        "1. Выбрать файл для работы.\n"
        "2. Инициализировать базу данных.\n"
        "3. Вывести содержимое базы данных.\n"
        "4. Добавить запись в произвольное место базы данных.\n"
        "5. Удалить произвольную запись из базы данных.\n"
        "6. Поиск по одному полю.\n"
        "7. Поиск по двум полям.\n"
        "0. Выход\n"
    )
    # get option
    while True:
        op = input_int("> ")
        if 0 <= op <= 7:
            break
        print('Unsupported option!')

    # do option
    if op == 0:
        return 0, fd

    if op == 1:
        fd.close()
        fd = open_db()

    elif op == 2:
        init_db(fd)

    elif op == 3:
        output_db(fd)

    elif op == 4:
        insert_db(fd)

    elif op == 5:
        delete_db(fd)

    elif op == 6:
        find_1_db(fd)

    elif op == 7:
        find_2_db(fd)

    return 1, fd


# Run
# file descriptor
fd = open_db()

# return code
ret = 1

while ret:
    ret, fd = menu(fd)

# close file
fd.close()