"""
Create a variable x = None. Print it. Ask the user to then assign a value to x via input. Print the new value..
"""

import sys

def main():

    #ASk for user input
    x = None
    x = int(input("Enter a value to assign to value x which is empty: "))

    print(f"You have assigned {x} to the value x.")

    return 0

if __name__ == "__main__":
    sys.exit(main())