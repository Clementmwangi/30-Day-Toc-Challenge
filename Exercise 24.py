"""
Ask the user for five words.
Store them in a list: `words`.
Then construct a new list `a_words` containing only those words that begin with "a" or "A".

Constraint:
You may not use any loop.
You may only use:
indexing
slicing
boolean expressions
list comprehensions
empty list initialisation
Example strategy: check each element individually and build the result list step-by-step.
"""

import sys

def main():
    #ask for user input
    word1 = input("Enter a word: ")
    word2 = input("Enter a word: ")
    word3 = input("Enter a word: ")
    word4 = input("Enter a word: ")
    word5 = input("Enter a word: ")

    words = [word1, word2, word3, word4, word5]
    a_words = []
    
    firstletters = [words[0][0:1], words[1][0:1], words[2][0:1], words[3][0:1], words[4][0:1]]

    if firstletters[0] == "a" or firstletters[0] == "A":
        a_words.append(words[0])

    if firstletters[1] == "a" or firstletters[1] == "A":
            a_words.append(words[1])

    if firstletters[2] == "a" or firstletters[2] == "A":
            a_words.append(words[2])

    if firstletters[3] == "a" or firstletters[3] == "A":
            a_words.append(words[3])

    if firstletters[4] == "a" or firstletters[4] == "A":
            a_words.append(words[4])

    print(a_words)

    return 0

if __name__ == "__main__":
    sys.exit(main())