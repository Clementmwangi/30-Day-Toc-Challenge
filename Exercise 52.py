"""
Ask the user for a list of three words (build a list manually).

If the list is non-empty, print "List has items".

Else print "Empty list".
"""

import sys

def main():

    #Ask the user for a list of three words
    user_word1 = input("Enter your first word: ")
    user_word2 = input("Enter your second word: ")
    user_word3 = input("Enter your third word: ")

    user_list = [user_word1, user_word2, user_word3]


    #just used if as it will return true if not empty
    if user_list:
        print("List has items.")
    else:
        print("Empty list")

    return 0

if __name__ == "__main__":
    sys.exit(main())