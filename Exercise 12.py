"""
Ask the user for a number and a word.

Print:

"<word> repeated <number> times."
"""

import sys

def main():

    #ask user for input
    number = int(input("Enter a number: "))
    word = input("Enter a word: ")

    print(f"{word} repeated {number} times.")

    return 0
    

if __name__ == "__main__":
    sys.exit(main())
