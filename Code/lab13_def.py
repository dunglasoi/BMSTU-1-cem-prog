# Программа сделана Нгуен Ань Зунг - ИУ7И-11Б

FILE_IN = 'test1.txt'
FILE_OUT = 'test2.txt'

f_in = open(FILE_IN, 'r')
f_out = open(FILE_OUT, 'w')

i = 0
for line in f_in:
    if i % 2 != 0:
        f_out.writelines(line)
    i += 1

f_in.close()
f_out.close()