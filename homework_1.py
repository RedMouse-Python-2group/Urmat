# coding: utf8

# Function get_integer - returns integer or error
def get_integer(text):
    try:
        input_value = int(raw_input(text))
    except ValueError:
        return 'error'
    else:
        return input_value

# HomeWork 1.1
x = get_integer('Введите число от 1 до 9: ')
if x == 'error':
    print 'Это не цифра !'
elif  (x < 1 or x > 9):
    print 'Введенная цифра меньше 1 или больше 9 !'
else:
    # Option 1
    if x <= 3:
        s = raw_input('Введите строку: ')
        n = get_integer('Введите цифру: ')
        if n != 'error':
            print s*n
    # Option 2
    elif x <= 6:
        m = get_integer('Введите степень: ')
        if m != 'error':
            print x ** m
    # Option 3
    elif x <= 9:
        i = 0
        while i < 10:
            i += 1
            x = x + 1
            print x