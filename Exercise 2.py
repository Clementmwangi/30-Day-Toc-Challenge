"""
Ask the user for two integers and print their sum.
"""
import sys

def main():
    #ask user for two integers
    int1 = int(input("Enter the first integer be used: "))
    int2 = int(input("Enter the second integer be used: "))

    sum = int2 + int1

    print(f"The sum of your integers is {sum}")

if __name__ == "__main__":
    sys.exit(main())

