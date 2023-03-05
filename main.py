import string
import pandas as pd

def task_1(str = '', i = 0, j = -1):
    return str[i-1:j]

def task_2(str = '', k = 1):
    str_list = list(str)
    str_list_new = []
    for i in range(len(str_list)):
        if ((i+1) % k  == 0):
            str_list_new.append(str_list[i])
    str = ''.join(str_list_new)
    return str

def task_3(*letters):
    return letters

def task_4(fname = ''):
    with open(fname, 'r') as f:
        data = f.read() # Чтение содержимого файла и помещение его в переменную data (type str)
        len_data = len(data) # Общее количество символов в файле
        data_words = data.split(' ') # Разбиение содержимого data по признаку пробела (разбиение строки на слова)
        len_data_wo_probel = sum(list(map(len,data_words))) # Количество символов в файле без учета пробелов
        s = ''.join(filter(lambda x: x not in string.punctuation, data))
        len_data_wo_punctuation = len(s) # Количество символов в файле без учета знаков препинания
        len_data_words = len(data_words) # Количество слов в файле
        data_sentences = data.split('.') # Разбиение содержимого data по признаку точки (разбиение строки на предложения)
        len_data_sentences = len(data_sentences)
        f.close()  # закрыть файл
        return len_data, len_data_wo_probel, len_data_wo_punctuation, len_data_words, len_data_sentences

def task_5(fname = ''):
    data = pd.read_csv(fname) # Загрузка файла с базой данных игр
    # Диалоговые окна с пользователем для выяснения интересующих жанров, категорий, платформ
    user_genre = input('Какие жанры игр вас интересуют? (Введите через пробел) (Action, RPG, FreetoPlay, Strategy, Adventure,Indie, Animation & Modeling,\n '
                    'Video Production, Audio Production, Casual, Simulation, Racing, Violent, Nudity, Multiplayer, Sports, Early Access, \n'
                    'Utilities, Game Development, Sexual Content, Gore, Education, Software Training, Photo Editing, Design & Illustration)\n')
    user_category = input('Какие категории игр вас интересуют? (Введите через пробел)  (Single, Multi, Steam Achievements, Partial Controller Support, Co-op, Valve Anti-Cheat enabled\n '
                    'Steam Cloud,Steam Achievements, Shared/Split, Steam Trading Cards,Full controller support, Steam Workshop)\n')
    user_platform = input('Какие платформы вас интересуют?(Введите через пробел)  (windows, linux, mac)\n')

    # Преобразование выбора пользователя из строки в список с разделителем - пробелом
    user_genre = user_genre.lower().split(' ')
    user_category = user_category.lower().split(' ')
    user_platform = user_platform.lower().split(' ')

    # Формирование списка рекомедованных игр
    recommend_games = []
    for i in range(len(data)):
        # Фильтр - если все параметры введенные пользователем входят в параметры данной игры,
        # то данная игра добавляется в список рекомендованных игр
        filter_genre = ''.join(filter(lambda x: x in data['genres'][i].lower(), user_genre))
        filter_category = ''.join(filter(lambda x: x in data['categories'][i].lower(), user_category))
        filter_platform = ''.join(filter(lambda x: x in data['platforms'][i].lower(), user_platform))
        if (not not filter_genre) and (not not filter_category) and (not not filter_platform):
            recommend_games.append(data['name'][i])

    # Запись данных в файл
    with open('task_5.txt', 'w') as f:
        f.write('Жанры пользователя:')
        f.write(' '.join(user_genre) + '\n')
        f.write('Категории пользователя:')
        f.write(' '.join(user_category) + '\n')
        f.write('Платформы пользователя:')
        f.write(' '.join(user_platform) + '\n')
        f.write('Рекомендованные игры:\n')
        f.write('\n'.join(recommend_games) + '\n')
        f.close()

    return recommend_games

def task_6(fname = ''):
    return 0

if __name__ == "__main__":
    tasks = [1,2,3]# Номера заданий, решение которых нужно произвести

    if 1 in tasks:
        # task_1
        dlg = 'Python is the best programming language in the world'
        i = 6
        j = -7
        rez = task_1(dlg,i,j) # Выведет символы от i-го от начала строки до -j-го от конца строки
        print(f'task_1: From /{dlg}/ \n given: /{rez}/ \n')

    if 2 in tasks:
        # task_2
        dlg = 'Guido van Rossum is the benevolent dictator for life'
        k = 4
        rez = task_2(dlg,k) # Выведет каждый k-й символ строки
        print(f'task_2: From /{dlg}/ \n given: /{rez}/ \n')

    if 3 in tasks:
        # task_3
        dlg = 'You have a problem with authority, Mr. Anderson.'
        #words = dlg3.split(' ') #
        letters = list(dlg.lower()) # Разбиение строки на символы - все символы преобразуются в строчные
        different_letters = list(set(letters)) # Создание списка неповторяющиеся элементов letters)
        rez = map(task_3, different_letters, [letters.count(letter) for letter in different_letters]) # dict(rez) - Возвращает словарь в виде ключей - букв и значений - цифр (ключ буква - это буква из строки, цифра - количество повторений данной буквы в строке)
        print(f'task_3: From /{dlg}/ \n given: /{dict(rez)}/ \n')
        #for letter in different_letters:
        #    print(f'Количество {letter} = {letters.count(letter)}')

    if 4 in tasks:
        # task_4
        fname = 'aristotle.txt'
        rez = task_4(fname)
        print(f'task_4: Количество символов в файле {fname} = {rez[0]}\n'
              f'Количество символов без учета пробелов в файле {fname} = {rez[1]}\n'
              f'Количество символов без знаков препинания в файле {fname} = {rez[2]}\n'
              f'Количество слов в файле {fname} = {rez[3]}\n'
              f'Количество предложений в файле {fname} = {rez[4]}\n')

    if 5 in tasks:
        # task_5
        fname = 'steam.csv'
        rez = task_5(fname)
        print(f'task_5: Файл с рекомендованными играми записан!\n'
              f'Рекомендованные игры:{rez}\n')

    if 6 in tasks:
        # task_6
        rez = task_5()
        print(rez)