from random import uniform


def increment(dict, a, b):
    if a in dict:
        if b in dict[a]:
            dict[a][b] += 1
        else:
            dict[a][b] = 1
    else:
        dict[a] = {}
        dict[a][b] = 1


def markov_chain(dict):
    chain = {}
    for w in dict:
        if len(w) == 0:
            continue
        for i in range(len(w) + 1):
            if i == 0:
                increment(chain, '^', w[i])
            elif i == len(w):
                increment(chain, w[i - 1], '$')
            else:
                increment(chain, w[i - 1], w[i])

    for letter1 in chain:
        total = 0
        for letter2 in chain[letter1]:
            total += chain[letter1][letter2]
        for letter2 in chain[letter1]:
            chain[letter1][letter2] /= (total * 1.0)

    return chain


def weighted_random_key(dict):
    rand = uniform(0, 1)
    total = 0
    for k in dict:
        total += dict[k]
        if total > rand:
            return k
    return None


def generate_word(dict):
    chain = markov_chain(dict)
    word = ''

    next_char = weighted_random_key(chain['^'])
    word += next_char
    while not word.endswith('$'):
        next_char = weighted_random_key(chain[word[-len(next_char):len(word)]])
        word += next_char

    return word[:-1]


def generate_word_within(dict, min, max):
    word = generate_word(dict)
    while len(word) > max or len(word) < min:
        word = generate_word(dict)
    return word
