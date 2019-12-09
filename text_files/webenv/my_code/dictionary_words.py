import random
import sys


def read_file(file_name):
    with open(file_name) as file:
        word_list = [line.strip() for line in file]
    return word_list


def choose_words(word_list, number):
    chosen_words = [random.choice(word_list) for i in range(number)]
    return chosen_words


def _format(chosen_words):
    sentence = ' '.join(chosen_words) + '.'
    return sentence


def main(file_name, number):
    completed_sentence = _format(choose_words(read_file(file_name), number))
    return completed_sentence


if __name__ == '__main__':
    print(main('/usr/share/dict/words', int(sys.argv[1])))
