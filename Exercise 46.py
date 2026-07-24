"""
Ask the user for a number.

Create a boolean variable is_even.

If is_even is True, print "Even number", else print "Odd number".

"""

import sys

def main():

    #Ask the user for a number.
    user_num = int(input("Enter a number: "))

    is_even = user_num % 2 == 0

    if is_even:
        print("Even number")
    else:
        print("Odd number") 

    return 0

if __name__ == "__main__":
    sys.exit(main())