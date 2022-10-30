main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
low_main_str = main_str.lower() #новая переменная для строки в нижнем регистре
letter_dict = {}
def get_count_char(str_):
    for letter in low_main_str:
        if letter.isalpha():
            if letter in letter_dict: #если есть в словаре
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1 #новое значение в словаре
        else:
            pass
    return letter_dict



















print(get_count_char(main_str))
