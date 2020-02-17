# python-scripts

This is a repository of random Python scripts I've made.

## Character Markov Chain

`CharacterMarkovChain.py` is an implementation of a Markov chain to generate realistic-looking words based
on a list of source words, such as an English dictionary or a list of names. The `markov_chain` method goes through
every word in the source list and creates a dictionary of the probabilities that each letter is followed by each other
letter, and then the `generate_word` method uses that dictionary as a Markov chain to generate new words. The
`generate_word_within` method is just like `generate_word`, but it restricts the length of the generated word to
within a specified range.

Here are some example `generate_word` outputs given the source list `['lasagna', 'spaghetti', 'rigatoni', 'macaroni',
'ravioli', 'linguine', 'fettuccine']`:
```
saspaguigui
rolasaghe
spararonetti
ragninaspa
lionghe
```

## Homomorse

Homomorses are pairs or sets of words with the same configuration of dots and dashes, or mits (Morse digits), ignoring
spaces. `Homomorse.py` finds every set of homomorses in the English dictionary text file, `enable1.txt`.

The homomorse set with the most mits turns out to be the words with the mit configuration
`-.....---.-..-----...-.-..-.-...-..-.--`, which includes:

`biologically, theologically`

The largest homomorse set turns out to be the words with the mit configuration `-....--....`, which includes:

`babe, bans, bates, bath, begs, deans, death, digs, dimes, duns, neeps, nips, tsadi`

Run the script to see the entire collection of English homomorses.

## LetterBoxed

`LetterBoxed.py` is a solver for Sam Ezersky's online puzzle [Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed).
The rules of the puzzle can be seen [here](https://i.imgur.com/41apwQx.png).

This script takes one command line argument,
namely a twelve-letter string consisting of each side of the Letter Boxed square. The order of sides or letters within a
side doesn't matter, as long as letters within a side are consecutive in the input. The script outputs every possible
two-word solution using the `enable1.txt` word list. This word list may vary from the one Sam uses, but it should still
output one or more valid solutions whenever possible.

## WordList OneLook

`WordListOneLook.py` takes in a wordlist text file and a pattern of letters, and it outputs every word in the wordlist
that matches the given pattern. Patterns are case-insensitive and take on the style of [onelook.com](onelook.com)
searches, where the `?` character indicates one wildcard character and the `*` character indicates a string of any
number (including zero) of wildcard characters. For example, the input `P??T*T*` indicates words with the first letter
P, fourth letter T, and a T anywhere after the fourth letter. With my wordlist, the output looks like this:
```
Input wordlist filepath: WordList.txt
Input pattern: P??T*T*
PARTEDTHEREDSEA
PARTYROCKANTHEM
POETRYANTHOLOGY
PARTSTHEREDSEA
PARTTHEREDSEA
POETLAUREATE
PORTAPOTTIES
PENTATONIX
PLOTTWISTS
PORTAPOTTY
POTTYMOUTH
PRETTYSURE
PLOTTWIST
```
I've found this script very useful for crossword construction and anything that involves filtering through a dictionary
or other wordlist file.

