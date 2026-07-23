"""
Ask the user to enter four integers.
Store them in 'nums'.
Replace:
the first number with its square.
the last number with its cube.
The compute and print the sum of all four numbers.
"""

import sys
import math

def main():
    #ask for user input
    num1 = int(input("Enter your data: "))
    num2 = int(input("Enter your data: "))
    num3 = int(input("Enter your data: "))
    num4 = int(input("Enter your data: "))

    nums = [num1, num2, num3, num4]

    #reassign the squared and cubed values
    nums[0] = math.pow(nums[0], 2)
    nums[-1] = math.pow(nums[-1], 3)

    #use sum function to get the total
    total = sum(nums)

    print(total)

    return 0

if __name__ == "__main__":
    sys.exit(main())