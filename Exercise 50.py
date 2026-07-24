"""
Ask the user for two integers a and b.

If both are positive, print "Both positive".

Otherwise, print "At least one is not positive".
"""

import sys

def main():

    #Ask the user for two integers a and b.
    user_num1 = int(input("Enter a number: "))
    user_num2 = int(input("Enter a number: "))

    if user_num1 > 0 and user_num2 > 0:
        print("Both positive")
    else:
        print("At least one is not positive")


    return 0

if __name__ == "__main__":
    sys.exit(main())