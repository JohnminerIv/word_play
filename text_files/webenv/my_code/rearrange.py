import random
import sys


def break_string(string_of_words):
    list_of_words = string_of_words.split(' ')
    return list_of_words


def randomize_words(word_list):
    for i in range(len(word_list)):
        word1_index = random.randrange(len(word_list))
        word2_index = random.randrange(len(word_list))
        word1 = word_list[word1_index]
        word2 = word_list[word2_index]
        word_list[int(word1_index)] = word2
        word_list[int(word2_index)] = word1
    return word_list


def _format(list_of_words):
    sentence = ' '.join(list_of_words)
    return sentence


if __name__ == '__main__':
    print(_format(randomize_words(break_string(sys.argv[1]))))
