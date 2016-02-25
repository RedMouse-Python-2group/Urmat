# coding: utf8

class Task1:    # HomeWork 1.1

    def __init__(self):
        self.x = self.get_integer('Введите число от 1 до 9: ')

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

    def option_1(self):
        return raw_input('Введите строку: ') * self.get_integer('Введите цифру: ')

    def option_2(self):
        return self.x ** self.get_integer('Введите степень: ')

    def option_3(self):
        return  [x for x in range(x+1,x+11)]

a = Task1()
if  (a.x < 1 or a.x > 9):
    print "Введенная цифра меньше 1 или больше 9 !"
elif a.x <= 3:    # Option 1
    print a.option_1()
elif a.x <= 6:    # Option 2
    print a.option_2()
elif a.x <= 9:    # Option 3
    print a.option_3()