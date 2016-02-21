# coding: utf8
import re, random

def get_url():
    """ This function returns attribute of file if it exists"""
    str = raw_input('Введите путь или несколько путей к файлу разделенный "//" (Example: //home/libron/Downloads): ')
    pattern = '\/\/(?:[\w\.]+)(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?'
    return re.findall(pattern, str)

def get_file_info(url, file):
    """ Function returns file information. Takes 3 arguments URL and File name """
    import os,time
    file_info = []

    for str in url:
        os.chdir(str)
        y = os.path.getctime(file)
        file_info.append(os.path.abspath(file)) # Directory
        file_info.append(os.path.getsize(file)) # Size
        file_info.append(time.ctime(y)) # Date
        if os.path.isfile(file): # Type
            file_info.append('File')
        else:
            file_info.append('Folder')
        return file_info

def play_vanga():
    """ Function which gives random answer to your question """
    list = ["Да","Нет", "Не знаю", "Пошел ты !","Бог знает", "Тупой вопрос", "Хмм...","Да ну на ?!","Так точно !"]
    answer = random.choice(list)
    question = raw_input("Задайте Ваш вопрос:\n")
    print '%s - %s' % (answer, question)

def get_random_text(file = 'words.txt'):
    """ Function reads file and making random text """
    f = open(file,"r")
    text = f.read()
    f.close()
    result = re.findall(r'\w+', text)
    random.shuffle(result)
    return (' '.join(result))


# Zadanie 2
url = get_url()
file = raw_input('Введите название папки или файла (Example: test.txt): ')
print get_file_info(url, file)

# Zadanie 3
play_vanga()

# Zadanie 4
str = get_random_text()
print str
word = raw_input('Введите слово которое требуется найти и заменить на ревертированное значение: ')
text = re.sub(r'^%s' % word, word[::-1], str)
text = re.sub(r'%s$' % word, word[::-1], text)
print text