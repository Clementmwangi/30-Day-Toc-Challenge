"""
Replace the second word in the list with string "UPDATED". Print the new list.
"""

import sys

def main():

    #list from 19
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    word3 = input("Enter your third word: ")
    
    wordlist = [word1, word2, word3]
    wordlist[1] = "UPDATED"

    print(wordlist)
    return 0

if __name__ == "__main__":
    sys.exit(main())