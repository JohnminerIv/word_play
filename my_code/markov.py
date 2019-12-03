#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if word in self.keys():
            self[word] += count
            self.tokens += count
        else:
            self[word] = count
            self.tokens += count
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self.keys():
            return self[word]
        else:
            return False

    def sample(self, amount=1):
        word_list = []
        words = []
        for i in range(amount):
            words.append(random.randint(0, (self.tokens - 1)))
        last_set_val = 0
        for type in self:
            new_val = last_set_val + self[type]
            for word in range(len(words)):
                if words[word] is not None and words[word] < new_val:
                    word_list.append(type)
                    words[word] = None
            last_set_val = new_val
        if amount == 1:
            return word_list[0]
        else:
            return word_list


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


class Chain(dict):
    def __init__(self, count=1, word_list=None):
        super(Chain, self).__init__()
        self.types = 0
        self.tokens = 0
        self.count = count
        if word_list is not None:
            for index in range(len(word_list)):
                if index + count < len(word_list):
                    self.add_dict([word_list[index + i] for i in range(count)], [word_list[index + i + 1] for i in range(count)])

    def add_dict(self, words1, words2, count=1):
        """Increase frequency count of given word by given count amount."""
        key = ' '.join(words1)
        value = ' '.join(words2)
        if key in self.keys():
            self[key].add_count(value, count)
            self.tokens += count
        else:
            self[key] = Dictogram([value])
            self.tokens += count
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self.keys():
            return self[word].tokens
        else:
            return False

    def word_dict(self, word):
        if word in self.keys():
            return self[word]
        else:
            return False

    def sample(self, amount=1000, word=None):
        word_list = []
        key = ''
        if word is None:
            key = random.choice(self.start(list(self.keys())))
            key_list = key.split()
            index = 0
            not_end = True
            while not_end:
                word = key_list[index]
                if '.' in word or '!' in word or '?'in word:
                    not_end = False
                if '^' in word:
                    word_list.append(word.replace('^', ''))
                else:
                    word_list.append(word)
                if index + 1 == len(key_list):
                    not_end = False
                index += 1
        else:
            key = word
            word_list.append(word)
        for i in range(amount-1):
            if '.' in key or '?' in key or '!' in key:
                break
            key = self[key].sample()
            words = key.split()
            word_list.append(words[-1])
        if amount == 1:
            return word_list[0]
        else:
            clean_list = [word for word in word_list[0].split()]
            for i in range(len(word_list)):
                if i > 0:
                    clean_list.append(word_list[i])
            return clean_list

    def start(self, keys_list):
        return [word for word in keys_list if '^' in word[0]]

    def end(self, keys_list):
        return [word for word in keys_list if '.' in word]


if __name__ == '__main__':
    main()
    fish_text = '^one fish two fish red fish blue fish.'
    chain = Chain(4, fish_text.split())
    print(chain)
    print(chain.sample(10))
