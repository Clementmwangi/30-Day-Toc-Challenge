"""
Ask the user for a short message. Print it repeated three times.
"""

import sys

def main():
    #ask user for a short message
    message = input("Enter a short message you want to be shown: ")

    for i in range(3):
        print(message)
    return 0
    

if __name__ == "__main__":
    sys.exit(main())