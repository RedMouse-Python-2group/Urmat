# coding: utf8

class Task2():  # HomeWork 1.2
    list = ('Ошибка это программа для людей', 'Вам в детский сад !', 'Вам в школу',
            'Вам в профессиональное учебное заведение', 'Вам на работу', 'Вам предоставляется выбор')

    def __init__(self):
        print u'Общество в начале XXI века\n'
        self.x = self.get_integer('Введите ваш возраст: ')

    def get_integer(self, text):
        """Function returns integer until it is True"""
        y = False
        while not y:
            try:
                input_value = int(raw_input(text))
            except ValueError:
                print 'Это не цифра !'
            else:
                y = True
                return int(input_value)

b = Task2()
if (b.x <= 0 or b.x > 120):
    print b.list[0]
elif b.x <= 6:    # Option 1
    print b.list[1]
elif b.x <= 17:   # Option 2
    print b.list[2]
elif b.x <= 24:   # Option 3
    print b.list[3]
elif b.x <= 59:   # Option 4
    print b.list[4]
elif b.x <= 120:  # Option 5
    print b.list[5]