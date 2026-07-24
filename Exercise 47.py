"""
Ask the user for a number.
Print:
"Negative" if the number is less than 0
"Zero" if the number is 0
"Positive" otherwise
"""

import sys

def main():

    #Ask the user for a number.
    user_num = int(input("Enter a number: "))

    if user_num < 0:
        print("Negative")
    elif user_num == 0:
        print("Zero")
    else:
        print("Positive")

    return 0

if __name__ == "__main__":
    sys.exit(main())