from markov import Chain
from my_module import clean_return_list, read_file, _format


def main(text_list, order):
    chain = Chain(order, text_list)
    # return chain.sample(10, 'rat-faced')
    # print(chain)
    return chain.sample(5)


if __name__ == '__main__':
    order = 3
    clean_list = clean_return_list(read_file('../text_files/The_Way_of_Kings.txt'))
    print(' '.join(main(clean_list, order)).strip())
    # fish_text = '^one fish two fish red fish blue fish.'
    # print(main(fish_text))
