"""
Ask the user for three numbers as strings (e.g., "12", "5", "100").
Store them in a list.
Then convert each element to an int *without loops* (explicit index assignments only).
Finally, compute and print their total.

"""

import sys

def main():
    #Ask the user for three numbers as strings so no typecasting
    num1st = input("Input a number: ")
    num2st = input("Input a number: ")
    num3st = input("Input a number: ")

    numstring = [num1st, num2st, num3st]
    numstring[0] = int(numstring[0])
    numstring[1] = int(numstring[1])
    numstring[2] = int(numstring[2])

    #make sure to add the number not the string type using sum
    total = sum(numstring)
    print(total)
    return 0

if __name__ == "__main__":
    sys.exit(main())