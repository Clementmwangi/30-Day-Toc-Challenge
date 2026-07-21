"""
Ask the user for a word. Print the first and last characters using indexing.
"""

import sys

def main():
    #ask user for a word
    word = input("Enter the word you want to get the first and last letter:")

    char1 = word[0:1]
    char2 = word[-1]

    print(f"For the word {word} the first character is {char1} and the last is {char2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())


