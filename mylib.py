# coding: utf8
def get_integer(text):
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

def count_words():
    """ This function count words in text and length length of the words """
    import re
    text = raw_input('Введите текст: ').strip()
    text = re.sub(ur'[.,/:;-] ?', '', text)
    res = text.split(' ')
    for value in res:
        print '%s - %s буквы' % (value, len(value))

def power_mydigits(*args):
    """ Функция принимает сколько угодно значений, и оно возводит каждое последуюзее число в степень предыдущего"""
    numbers = list(args)
    numbers.insert(0, 1)
    i = 0
    for t in args:
        print t ** numbers[i]
        i = i + 1