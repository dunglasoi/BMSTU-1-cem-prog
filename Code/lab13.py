# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б
#1. Выбрать файл для работы
#2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)
#3. Вывести содержимое базы данных
#4. Добавить запись в конец базы данных
#5. Поиск по одному полю
#6. Поиск по двум полям


# db column separater
SEP = ','

def input_int(msg):
    while True:
        try:
            x = int(input(f"{msg}"))
            break
        except Exception:
            print(f"{msg} должен быть int число!")
    return x

class Database:
    """Database"""

    def open(self, filename):
        """Open file"""
        try:
            # read file
            if hasattr(self, 'f'):
                self.__del__()

            self.f = open('tmp/'+filename, 'a+')

            # get column info
            self.f.seek(0)
            line = self.f.readline()
            self.columns = line[:-1].split(SEP)
            self.col = len(self.columns)
            if self.col == 1 and self.columns[0] == '':
                self.col = 0

            return True

        except Exception as e:
            print(e)

    def write_record(self, columns):
        """Insert record into db"""
        s = ''
        for i in columns:
            s += i+SEP
        s = s[:-1]+'\n'
        self.f.write(s)

    def output(self):
        """Output db"""
        if self.col < 2:
            print("Database is empty!")
            print()
            return

        width = self._count_column_width()

        # output records
        self.f.seek(0)
        c = -1
        for line in self.f:
            l = line[:-1].split(SEP)
            c += 1
            if c > 0:
                print(f"{c:3}", end='')
            else:
                print(f"{'':3}", end='')
            for i in range(len(l)):
                print(f"| {l[i]:{width[i]+3}}", end='')
            print()
        print()

    def insert(self):
        """Insert 1 record into db"""
        if self.col == 0:
            print("Database need to initialize (2)!")
            print()
            return

        columns = []
        for j in range(self.col):
            columns.append(input(f"{self.columns[j]}: "))
        self.write_record(columns)

    def init(self):
        """Initialize db"""
        print('Инициализация базу данных.')

        # delete file content
        self.f.truncate(0)

        # columns name
        self.col = input_int('Сколько полей? ')
        self.columns = []
        for i in range(self.col):
            self.columns.append(input(f'Название поля {i}: '))
        self.write_record(self.columns)

        # columns content
        self.rec = input_int('Сколько записи? ')
        for i in range(self.rec):
            print(f"Запись {i}:")
            self.insert()

        print()

    def find_within_1(self, word):
        """Поиск по одному полю"""
        if self.col == 0:
            print("Database need to initialize (2)!")
            print()
            return

        print("Доступные поля:")
        for i in range(len(self.columns)):
            print(f"{i}. {self.columns[i]}")

        while True:
            c = input_int("Выберите поле> ")
            if 0 <= c < self.col:
                break
            print('Некорректное поле!')

        width = self._count_column_width()

        # find
        self.f.seek(0)
        i = -1
        r = 0           # число совпадение
        for line in self.f:
            l = line[:-1].split(SEP)
            i += 1
            if l[c] == word:
                r += 1
                print(f"{i:3}", end='')
                for j in range(len(l)):
                    print(f"| {l[j]:{width[j]+3}}", end='')
                print()
        if r == 0:
            print("Нет совпадение!")
        print()

    def find_within_2(self, word):
        """Поиск по двум полю"""
        if self.col == 0:
            print("Database need to initialize (2)!")
            print()
            return

        print("Доступные поля:")
        for i in range(len(self.columns)):
            print(f"{i}. {self.columns[i]}")

        while True:
            c1 = input_int("Выберите поле 1> ")
            if 0 <= c1 < self.col:
                break
            print('Некорректное поле 1!')

        while True:
            c2 = input_int("Выберите поле 2> ")
            if 0 <= c2 < self.col:
                break
            print('Некорректное поле 2!')

        width = self._count_column_width()

        # find
        self.f.seek(0)
        i = -1
        r = 0           # число совпадение
        for line in self.f:
            l = line[:-1].split(SEP)
            i += 1
            if l[c1] == word or l[c2] == word:
                r += 1
                print(f"{i:3}", end='')
                for j in range(len(l)):
                    print(f"| {l[j]:{width[j]+3}}", end='')
                print()
        if r == 0:
            print("Нет совпадение!")
        print()

    def __del__(self):
        """Destructor

        close file
        """
        self.f.close

    def _count_column_width(self):
        """Count column width"""
        self.f.seek(0)
        width = [0 for _ in range(self.col)]    # column width
        for line in self.f:
            l = line[:-1].split(SEP)
            for i in range(len(l)):
                w = len(l[i])
                if w > width[i]:
                    width[i] = w
        return width


def menu(db: Database):
    """Menu"""
    # print options
    print(
        "Выберите действие:\n"
        "1. Выбрать файл для работы.\n"
        "2. Инициализировать базу данных.\n"
        "3. Вывести содержимое базы данных.\n"
        "4. Добавить запись в конец базы данных.\n"
        "5. Поиск по одному полю.\n"
        "6. Поиск по двум полям.\n"
        "0. Выход\n"
    )
    # get option
    while True:
        op = input_int("> ")
        if 0 <= op <= 6:
            break
        print('Unsupported option!')

    # do option
    if op == 0:
        return 0

    if op == 1:
        while True:
            print("Выберите файл для работы:")
            filename = input("> ")
            print()
            if db.open(filename):
                break

    elif op == 2:
        db.init()

    elif op == 3:
        db.output()

    elif op == 4:
        db.insert()

    elif op == 5:
        w = input('Ключевое слово: ')
        db.find_within_1(w)

    elif op == 6:
        w = input('Ключевое слово: ')
        db.find_within_2(w)

    return 1


# Run
db = Database()
# choose file
while True:
    print("Выберите файл для работы:")
    filename = input("> ")
    if db.open(filename):
        break
print()

# next run
while menu(db):
    pass