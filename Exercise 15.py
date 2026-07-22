"""
Ask for a word. Print whether the word starts with "a" or "A" using a boolean expression.
"""

import sys

def main():
    #ask for input
    word = input("Enter a word: ")

    if word[0:1] == "a"  or word[0:1] == "A":
        print(f"{word} starts with either an a or A.")
    else:
        print(f"{word} doesn't start with either an a or A.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
