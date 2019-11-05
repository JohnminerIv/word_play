import random


def anagram(word):
    ana = []
    for letter in word:
        ana.append(letter)
    for i in range(len(ana)):
        letter1_index = random.randrange(len(ana))
        letter2_index = random.randrange(len(ana))
        letter1 = ana[letter1_index]
        letter2 = ana[letter2_index]
        ana[int(letter1_index)] = letter2
        ana[int(letter2_index)] = letter1
    return ''.join(ana)


if __name__ == '__main__':
    print(anagram('hello'))
