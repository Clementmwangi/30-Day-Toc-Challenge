"""
Ask the user for an integer, convert it using float(), and print both values.
"""

import sys

def main():
    #ask for user input
    value1 = int(input("Enter a whole number: "))
    

    print(f"You entered {value1} which is a whole number and {float(value1)} is it with decimals")

    return 0
    

if __name__ == "__main__":
    sys.exit(main())
