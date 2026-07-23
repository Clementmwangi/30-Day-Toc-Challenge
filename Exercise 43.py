"""
Ask the user for an integer.

If the number is greater than 10, print "Large number".
"""

import sys

def main():

    user_num = int(input("Enter an integer: "))

    if user_num > 10:
        print("Large number")
    else:
        print("Small number")

    return 0

if __name__ == "__main__":
    sys.exit(main())