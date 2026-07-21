"""
Ask the user for two integers and print:

quotient using /
integer division using //
remainder using %
"""

import sys

def main():

    #ask user for integers for each operation
    num1 = int(input("Enter a number you want to be used: "))
    num2 = int(input("Enter a number you want to be used: "))

    num3 = num1 / num2
    num4 = num1 // num2
    num5 = num1 % num2

    print(f"For the two integers you provided, when you divide {num1} by {num2} you get {num3}")
    print(f"For the two integers you provided, when you divide {num1} by {num2} its rounded down to {num4}")
    print(f"For the two integers you provided, when you divide {num1} by {num2} you get the remainder {num5}")
    return 0

if __name__ == "__main__":
    sys.exit(main())