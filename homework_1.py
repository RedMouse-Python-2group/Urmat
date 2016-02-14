# coding: utf8
import mylib     # My functions

# HomeWork 1.1
x = mylib.get_integer('Введите число от 1 до 9: ')
if  (x < 1 or x > 9):
    print "Введенная цифра меньше 1 или больше 9 !"
elif x <= 3:    # Option 1
    print raw_input('Введите строку: ') * mylib.get_integer('Введите цифру: ')
elif x <= 6:    # Option 2
    print x ** mylib.get_integer('Введите степень: ')
elif x <= 9:    # Option 3
    print [x for x in range(x+1,x+11)]