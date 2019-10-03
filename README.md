# python-scripts

This is a repository where of random Python scripts I've made.

## WordList OneLook

`WordListOneLook.py` takes in a wordlist text file and a pattern of letters, and it outputs every word in the wordlist that matches the given pattern. Patterns are case-insensitive and take on the style of [onelook.com](onelook.com) searches, where the `?` character indicates one wildcard character and the `*` character indicates a string of any number (including zero) of wildcard characters. For example, the input `P??T*T*` indicates words with the first letter P, fourth letter T, and a T anywhere after the fourth letter. With my wordlist, the output looks like this:
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
I've found this script very useful for crossword construction and anything that involves filtering through a dictionary or other wordlist file.

## Homomorse

Homomorses are pairs or sets of words with the same configuration of dots and dashes, or mits (Morse digits), ignoring spaces. `Homomorse.py` finds every set of homomorses in the English dictionary text file, `enable1.txt`.

The homomorse set with the most mits turns out to be `biologically` and `theologically`, both of which have the following mit configuration: `-.....---.-..-----...-.-..-.-...-..-.--`

The largest set of homomorse turns out to be the words with the mit configuration `-....--....`, which includes: `babe, bans, bates, bath, begs, deans, death, digs, dimes, duns, neeps, nips, tsadi`

Run the script to see the entire collection of English homomorses.
