import random
from sys import argv
from my_module import read_file, choose_words, break_string, _format


def rand_dict(text_file, amount=1):
    return choose_words(break_string(read_file(text_file)), amount)


if __name__ == '__main__':
    print(_format(rand_dict('/usr/share/dict/words', int(argv[1]))))
