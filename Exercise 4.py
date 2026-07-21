"""
Ask the user for a number and print the square and cube.
"""

import sys
import math

def main():
    #ask user for a number to square and cube
    num1 = int(input("Enter the number you want to be squared and cubed: "))

    num2 = math.pow(num1, 2)
    num3 = math.pow(num1, 3)

    print(f"The number {num1} squared is {num2} and when cubed is {num3}.")
    return 0

if __name__ == "__main__":
    sys.exit(main())


