import random


def game_loop():
    while True:
        print(paragraph_fill(paragraph_choice()))
        print('Would you like to play again? Y/N')
        user_in = input()
        if user_in == 'N':
            break


def paragraph_choice():
    paragraphs = ['''
 This morning I woke up to a very /1Adjective thing.
 When I investigated it turned out to be a /1Noun .
 Very /1Adverb I decided to wake up my room mate /1Name so we could
 marvle at the /1Noun but before our very eyes it turned into a /2Noun .
 Since we were kind of freaked out we decided to /1Verb as
 /2Adjective as we could away from the still morphing object.
    ''']
    print('Pick a paragraph to play. Enter 1-5 or R for random.')
    while True:
        try:
            user_in = input()
            if user_in == 'r':
                return random.choise(paragraphs)
            return paragraphs[int(user_in)-1]
        except:
            print("that wasn't an option")
            pass


def paragraph_fill(paragraph):
    paragraph = paragraph.split(' ')
    new_para = []
    tokens = {}
    for word in range(len(paragraph)):
        if '/' in paragraph[word]:
            this_word = paragraph[word]
            if paragraph[word] in tokens.keys():
                new_para.append(tokens[paragraph[word]])
            else:
                print('Please tell me a ' + this_word.strip('/1234567890') + ':')
                tokens[paragraph[word]] = str(input())
                new_para.append(tokens[paragraph[word]])
        else:
            new_para.append(paragraph[word])
    print(tokens)
    new_para = ' '.join(new_para)
    return new_para


if __name__ == '__main__':
    game_loop()
