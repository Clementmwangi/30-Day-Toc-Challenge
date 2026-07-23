"""
Ask the user for their age.

If the age is at least 18, print "Adult".

Otherwise, print "Minor".
"""

import sys

def main():

    #Ask the user for their age.
    user_age = int(input("Enter your age: "))

    if user_age >= 18:
        print("Adult")
    else:
        print("Minor")
        
    return 0

if __name__ == "__main__":
    sys.exit(main())