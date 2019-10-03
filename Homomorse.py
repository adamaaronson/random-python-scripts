morse = {'a': '.-',
         'b': '-...',
         'c': '-.-.',
         'd': '-..',
         'e': '.',
         'f': '..-.',
         'g': '--.',
         'h': '....',
         'i': '..',
         'j': '.---',
         'k': '-.-',
         'l': '.-..',
         'm': '--',
         'n': '-.',
         'o': '---',
         'p': '.--.',
         'q': '--.-',
         'r': '.-.',
         's': '...',
         't': '-',
         'u': '..-',
         'v': '...-',
         'w': '.--',
         'x': '-..-',
         'y': '-.--',
         'z': '--..'}

dictionary = open('enable1.txt').read().splitlines()


def makemorse(word):
    morseword = ''
    word = [l for l in word.lower() if l in 'abcdefghijklmnopqrstuvwxyz'];
    for l in word:
        morseword = morseword + morse[l]
    return morseword


def homomorse(words):
    morsewords = {}
    for w in words:
        morsew = makemorse(w)
        if morsew in morsewords.keys():
            morsewords[morsew].append(w)
        else:
            morsewords[morsew] = [w]

    homomorse = {key: value for (key, value) in morsewords.items() if len(value) > 1}
    return homomorse


def commas(word):
    return word.count(',')


def mits(word):
    return word.index(' ')


words = dictionary
homomorse = homomorse(words)

hmstrings = [m + '   ' + ', '.join(homomorse[m]) for m in homomorse.keys()]

# sort by Morse length
print('\n'.join(sorted(hmstrings, key=mits, reverse=True)))

# sort by set size
#print('\n'.join(sorted(hmstrings, key=mits, reverse=True)))
