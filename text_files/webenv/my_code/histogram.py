import random


def clean_return_list(text_string):
    text_string = text_string.translate({ord(i): '' for i in """.?!,":;â€œ™@$%&*[]#()~_˜©”"""})
    text_string = text_string.translate({ord(i): ' ' for i in """”"""})
    text_string = text_string.lower()
    list_of_words = text_string.split(' ')
    clean_list = []
    for word in list_of_words:
        clean_word = word.strip()
        clean_word = clean_word.strip('\x9d')
        if clean_word != '' and clean_word != ' ':
            clean_list.append(clean_word)
    return clean_list


def read_file(file_name):
    with open(file_name) as file:
        text_string = [line.strip() for line in file]
    text_string = ' '.join(text_string)
    return text_string


def histo_dic(text_list):
    my_histogram = {}
    for word in text_list:
        if word in my_histogram.keys():
            my_histogram[word] += 1
        else:
            my_histogram[word] = 1
    my_reverse_histogram = {}
    for key in my_histogram.keys():
        if my_histogram[key] in my_reverse_histogram.keys():
            my_reverse_histogram[my_histogram[key]].append(key)
        else:
            my_reverse_histogram[my_histogram[key]] = [key]
    return my_histogram, my_reverse_histogram


def histo_list(text_list):
    my_histogram = [[0, 0]]
    for word in text_list:
        add_one = False
        for index in range(len(my_histogram)):
            if word == my_histogram[index][0]:
                my_histogram[index][1] += 1
                add_one = True
        if add_one is False:
            my_histogram.append([word, 1])
    my_histogram.remove(my_histogram[0])
    return my_histogram


def histo_tup(text_list):
    my_tuplgram = [[0, 0]]
    for word in text_list:
        add_one = False
        for index in range(len(my_tuplgram)):
            if word == my_tuplgram[index][0]:
                word_count = my_tuplgram[index][1] + 1
                my_tuplgram[index] = (word, word_count)
                add_one = True
        if add_one is False:
            my_tuplgram.append((word, 1))
    my_tuplgram.remove(my_tuplgram[0])
    return my_tuplgram


def unique_words_dic(histogram_dic):
    return len(histogram_dic)


def unique_words_tup(histogram_dic):
    return len(histogram_dic)


def unique_words_list(histogram_dic):
    return len(histogram_dic)


def frequency_dic(word, histogram_dic):
    freq = histogram_dic[word]
    return freq


def frequency_tup(word, histogram_tup):
    for index in range(len(histogram_tup)):
        if histogram_tup[index][0] == word:
            return histogram_tup[index][1]


def frequency_list(word, histogram_list):
    for index in range(len(histogram_list)):
        if histogram_list[index][0] == word:
            return histogram_list[index][1]


def dict_prob_gen(histogram):
    word = random.random()
    sum = 0
    for key in histogram.keys():
        sum += histogram[key]
    word_probability = 1/sum
    last_set_val = 0
    for type in histogram:
        new_val = last_set_val + word_probability*histogram[type]
        if word >= last_set_val and word < new_val:
            return type
        last_set_val = new_val


def test_prob_gen(histogram):
    new_histogram = {}
    for i in range(10000):
        type = dict_prob_gen(histogram)
        if type in new_histogram.keys():
            new_histogram[type] += 1
        else:
            new_histogram[type] = 1
    print(new_histogram)
    sum = 0
    for key in new_histogram.keys():
        sum += new_histogram[key]
    print(sum)
    return new_histogram


if __name__ == '__main__':
    text_string = read_file('1661-.txt')
    list_of_words = clean_return_list(text_string)
    _histogram, r = histo_dic(list_of_words)
    unique = unique_words_dic(_histogram)
    print(f'There were {unique} unique words.')
    _frequency = frequency_dic('i', _histogram)
    print(f'The frequency of i is {_frequency}.')
    # print(dict_prob_gen(_histogram))
    # new_hist = test_prob_gen(_histogram)
    # print(sorted(_histogram.items(), key=lambda kv: kv[1]))
