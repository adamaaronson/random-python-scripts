# python-scripts

This is a repository where I dump Python scripts I've made for whatever reason.

## WordList OneLook

This script takes in a wordlist text file and a pattern of letters, and it outputs every word in the wordlist that matches the given pattern. Patterns are case-insensitive and take on the style of [onelook.com](onelook.com) searches, where the `?` character indicates one wildcard character and the `*` character indicates a string of any number (including zero) of wildcard characters. For example, the input `P??T*T*` indicates words with the first letter P, fourth letter T, and a T anywhere after the fourth letter. With my wordlist, the output looks like this:
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
