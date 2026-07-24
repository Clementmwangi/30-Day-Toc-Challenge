"""
Ask the user for a word.
Print each character on a separate line.
"""

import sys

def main():

    #ask for a word
    user_word = input("Enter a word: ")

    for word in user_word:
        print(word)

    return 0

if __name__ == "__main__":
    sys.exit(main())