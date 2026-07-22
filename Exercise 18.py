"""
Ask the user for a number.

Convert to int.

Then reassign the variable to None.

Print both states and explain (in comments) why a variable can change type.
"""

import sys

def main():

    number1 = int(input("Enter a number: "))
    number2 = None

    print(number1, type(number1))
    print(number2, type(number2))
    # Variables can change type as they only store a value thus when the value changes so does the type
    return 0

if __name__ == "__main__":
    sys.exit(main())