"""
Given a list of integers, print only the positive numbers. This will require the use of the
 'continue' keyword.
"""

import sys

def main():

    numbers = []
    for x in range(5):
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)
    
    valid_nums = []
    for number in numbers:
        if number > 0:
           valid_nums.append(number)
        else:
           continue
    
    print("Positive number: ", valid_nums)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())