import sys

dict = open('enable1.txt').read().splitlines()
dict = [w for w in dict if len(w) > 2]

def letter_boxed(args):
    if len(args) != 2 or len(args[1]) != 12 or not args[1].isalpha():
        return 'Error: input letters in a 12-character string, grouping sides of the letter box together.'

    letters = args[1].lower()
    sides = [letters[0:3], letters[3:6], letters[6:9], letters[9:]]
    sides_dict = {}
    for i, side in enumerate(sides):
        for letter in side:
            sides_dict[letter] = i
    words = []

    for w in dict:
        side = -1
        for l in w:
            if l not in letters:
                break
            else:
                next_side = sides_dict[l]
                if next_side == side:
                    break
                side = next_side
        else:
            words.append(w)

    solutions = []

    for w1 in words:
        for w2 in [w for w in words if w.startswith(w1[len(w1) - 1])]:
            if set(list(w1 + w2)) == set(letters):
                solutions.append([w1, w2])
                break

    if len(solutions) == 0:
        return 'No solution found!'
    return 'Solutions found:\n' + '\n'.join(['{}, {}'.format(s[0].upper(), s[1].upper()) for s in solutions])


print(letter_boxed(sys.argv))