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