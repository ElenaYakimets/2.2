import chardet


def read_files(name):
    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        original_text = data.decode(result['encoding'])
        return original_text


def count_word(original_text):
    to_list = original_text.split(' ')
    to_set = set()
    for words in to_list:
        if len(words) > 6:
            to_set.add(words)
    words_value = {}
    for letter_count in to_set:
        count = 0
        for s in to_list:
            if letter_count == s:
                count += 1
        words_value[letter_count] = count
    return words_value


def sort_top(words_value):
    sorted_count_pairs = sorted(words_value.items(), key=lambda x: x[1], reverse=True)
    top10 = sorted_count_pairs[:10]
    for word, freq in top10:
        print("Слово {} выстретилось {} раз".format(word, freq))


def main():
    while True:
        name = input('Введите имя файла: newsit.txt, newsafr.txt, newsfr.txt, newscy.txt. Выход - exit: ')
        if name == 'newsfr.txt' or name == 'newsit.txt' or name == 'newsafr.txt' or name == 'newscy.txt':
            print('Идет обработка файла ...')
            top10 = sort_top(count_word(read_files(name)))
            break
        else:
            print('Некорректный ввод, повторите.')


main()
