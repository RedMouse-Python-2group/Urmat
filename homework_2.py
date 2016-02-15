# coding: utf8
import mylib     # My functions

# HomeWork 1.2
print u'Общество в начале XXI века\n'

list = ('Ошибка это программа для людей', 'Вам в детский сад !', 'Вам в школу',
        'Вам в профессиональное учебное заведение', 'Вам на работу', 'Вам предоставляется выбор')

x = mylib.get_integer('Введите ваш возраст: ')
if (x <= 0 or x > 120):
    print list[0]
elif x <= 6:    # Option 1
    print list[1]
elif x <= 17:   # Option 2
    print list[2]
elif x <= 24:   # Option 3
    print list[3]
elif x <= 59:   # Option 4
    print list[4]
elif x <= 120:  # Option 5
    print list[5]