# coding: utf8

# Function get_integer - returns integer or error
def get_integer(text):
    try:
         input_value = int(raw_input(text))
    except ValueError:
        return 'error'
    else:
        return input_value

# HomeWork 1.2
print u'Общество в начале XXI века\n'
x = get_integer('Введите ваш возраст: ')
if (x == 'error' or x <= 0 or x > 120):
    print 'Ошибка, это программа для людей'
else:
    # Option 1
    if x <= 6:
        print 'Вам в детский сад'
    # Option 2
    elif x <= 17:
        print 'Вам в школу'
    # Option 3
    elif x <= 24:
        print 'Вам в профессиональное учебное заведение'
    # Option 4
    elif x <= 59:
        print 'Вам на работу'
    # Option 5
    elif x <= 120:
        print 'Вам предоставляется выбор'