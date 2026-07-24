"""
Ask the user repeatedly for input until they enter "quit".
Print each input except "quit".
"""

import sys

def main():

    while True:
        user_input = input("Enter a word(enter quit to quit: )").lower()
        if user_input == "quit":
            break
    
    return 0

if __name__ == "__main__":
    sys.exit(main())