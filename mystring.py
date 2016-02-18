# coding: utf8
import re

def get_word(text, symbol = ' ', long = True):
    """This Function returns long or short word, with last symbol ' ' - by default.
    Takes 3 parameters:
    - Text to search for
    - Last symbol
    - Size of word. True - find long word, False - to find short """
    pattern = '\w+%s' % symbol
    result = re.findall(pattern, text)
    if long:
        return max(result, key=len)
    else:
        return min(result, key=len)

def count_words(text):
    """ Function counts words in text """
    result = re.findall(r'\w+', text)
    return len(result)

def find_my_word(text, word):
    """ Function finds your words in text """
    result = re.findall(word, text)
    return result