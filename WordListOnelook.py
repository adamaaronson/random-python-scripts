def patternmatch(pat, word):
    pat = pat.upper()
    word = word.upper()

    # check for pattern length
    if '*' not in pat and len(pat) != len(word):
        return False

    # check for double *'s
    l = 0
    while l < len(pat):
        if l > 0:
            if pat[l] == '*' and pat[l - 1] == '*':
                pat = pat[0:l] + pat[l + 1::]
                l -= 1
        l += 1

    return submatch(pat, word)


def firstalphaindex(word):
    for i in range(len(word)):
        if word[i].isalpha():
            return i
    return -1


def indices(word, char):
    inds = []
    for i in range(len(word)):
        if word[i] == char:
            inds.append(i)
    return inds


def submatch(pat, word):
    if pat == '*':
        return True
    if len(pat) == 0:
        return len(word) == 0
    if len(word) == 0:
        return False
    if pat == word:
        return True

    # process *'s
    if pat[0] == '*':
        ind = firstalphaindex(pat)
        if ind == -1:
            return True
        else:
            if pat[ind] in word[ind - 1::]:
                inds = indices(word, pat[ind])
                return True in [submatch(pat[ind::], word[i::]) for i in inds]
            else:
                return False
    # process wildcards
    if pat[0].isalpha() and pat[0] != word[0]:
        return False
    # check consonants
    if pat[0] == '$' and word[0].upper() not in 'BCDFGHJKLMNPQRSTVWXYZ':
        return False
    # check vowels
    if pat[0] == '@' and word[0].upper() not in 'AEIOU':
        return False
    return submatch(pat[1::], word[1::])


wordlist = input('Input wordlist filepath: ')

words = open(wordlist).read().splitlines()
words = [w[(w.index(' ') + 1)::] if ' ' in w else w for w in words]

pattern = input('Input pattern: ')

i_have_no_words = True
for w in words:
    if patternmatch(pattern, w):
        i_have_no_words = False
        print(w)
if i_have_no_words:
    print('I have no words...')
