"""
Ask the user for three words (one per input).

Store them in a list and print the list exactly as Python represents it.
"""

import sys

def main():
    #ask for user input
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    word3 = input("Enter your third word: ")

    wordlist = [word1, word2, word3]

    print(wordlist)

    return 0

if __name__ == "__main__":
    sys.exit(main())