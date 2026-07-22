"""
Ask the user for their age. Print whether they are at least 18 (True/False).
"""

import sys

def main():
    #ask for age
    age = int(input("Enter your age: "))
    verifiedage = 18

    if age >= 18:
        print(f"You are above {verifiedage} years as you are {age}.")
    else:
        print(f"You have not yet attained {verifiedage} years of age.")

    return 0
    

if __name__ == "__main__":
    sys.exit(main())
