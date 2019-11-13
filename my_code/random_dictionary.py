import random
from my_module import read_file, choose_words, break_string


def rand_dict(text_file):
    return choose_words(break_string(read_file(text_file)), 1)


if __name__ == '__main__':
    print(rand_dict('/usr/share/dict/words')[0])
