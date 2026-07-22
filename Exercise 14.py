"""
Ask for two numbers and print:

a > b
a == b
a != b
(all boolean results)
"""

import sys

def main():

    #ask for user input
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    if num1 > num2:   
        print(f"For {num1} > {num2} the answer is {num1 > num2}")
    else:
        print(f"For {num1} > {num2} the answer is {num1 > num2}")

    if num1 == num2:   
        print(f"For {num1} == {num2} the answer is {num1 == num2}")
    else:
        print(f"For {num1} == {num2} the answer is {num1 == num2}")

    if num1 != num2:   
        print(f"For {num1} != {num2} the answer is {num1 != num2}")
    else:
        print(f"For {num1} != {num2} the answer is {num1 != num2}")
    

    return 0
    
if __name__ == "__main__":
    sys.exit(main())
