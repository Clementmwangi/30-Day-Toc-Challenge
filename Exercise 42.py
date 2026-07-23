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

    # use .get() so as to get None if user enters invalid choice
    choice = grades.get(user_choice)

    if choice is not None:
        print(f"For the grade {user_choice} the minimum score is {choice}")
    else:
        print("You have put an invalid choice")

    return 0

if __name__ == "__main__":
    sys.exit(main())