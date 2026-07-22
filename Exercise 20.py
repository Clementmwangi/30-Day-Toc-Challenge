"""
Using the list created in Exercise 19, print:
the first word
the last word
the length of the list
"""

import sys

def main():

    #list from 19
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    word3 = input("Enter your third word: ")

    wordlist = [word1, word2, word3]

    print(f" The first word is {wordlist[0]}")
    print(f" The last word is {wordlist[-1]}")
    
    print(f"The list contains {len(wordlist)} words")

    return 0

if __name__ == "__main__":
    sys.exit(main())