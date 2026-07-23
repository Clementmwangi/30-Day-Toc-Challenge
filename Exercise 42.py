"""
grades = {
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50
}

Ask the user for a grade letter (A, B, C, or D).
Print the corresponding minimum score.
"""

import sys

def main():

    grades = {"A": 80,
              "B": 70,
              "C": 60,
              "D": 50}

    #ask for user input
    user_choice = input("Enter a grade letter(A, B, C, D): ").upper()

    if user_choice == "A":
        print(grades.get("A"))
    elif user_choice == "B":
        print(grades.get("B"))
    elif user_choice == "C":
        print(grades.get("C"))
    else:
        print(grades.get("D"))

    return 0

if __name__ == "__main__":
    sys.exit(main())