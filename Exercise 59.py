"""
Using the word in Exercise 58, count how many characters it has using a loop (do not use len()).
"""

import sys

def main():

    user_word = input("Enter a word: ")

    count = 0
    for word in user_word:
        count += 1

    print(f"The word {user_word} has {count} letters.")

    return 0

if __name__ == "__main__":
    sys.exit(main())