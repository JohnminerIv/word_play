from markov import Chain
from my_module import clean_return_list, read_file, _format


def main(text_list):
    chain = Chain(4, text_list)
    # return chain.sample(10, 'rat-faced')
    return chain.sample()


if __name__ == '__main__':
    clean_list = clean_return_list(read_file('../text_files/1661-.txt'))
    print(' '.join(main(clean_list)))
    # fish_text = '^one fish two fish red fish blue fish.'
    # print(main(fish_text))
