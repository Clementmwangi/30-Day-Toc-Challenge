"""
Ask the user for numbers repeatedly (use a list of inputs given upfront, e.g. 5 numbers).
Stop processing when a negative number is encountered.
Print the numbers processed before stopping.
This will require your use of the 'break' keyword.
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
            break

    print("Positive number: ", valid_nums)
        

    return 0

if __name__ == "__main__":
    sys.exit(main())