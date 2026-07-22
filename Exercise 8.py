"""
Ask the user for two words and print them combined with a space:

<word1> <word2>
"""

import sys

def main():
    #ask user for two words
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    combined = word1 + ' ' + word2

    print(combined) 
    return 0
    

if __name__ == "__main__":
    sys.exit(main())
