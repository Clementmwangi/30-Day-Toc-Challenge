"""
Part A
Ask the user for:
student name
three test scores (integers)
Store the scores in a list.

Part B
Create a dictionary called student with keys:
"name" → student name
"scores" → list of scores
Print the dictionary.

Part C
Compute the average score and add a new key:
"average" → average score (float)
Print the final dictionary.
"""

import sys

def main():

    #Part a
    student_name = input("Enter your name: ")
    score1 = int(input("Enter your first score: "))
    score2 = int(input("Enter your second score: "))
    score3 = int(input("Enter your third score: "))

    score_list = [score1, score2, score3]

    #Part b
    student = {"name" : student_name,
               "scores" : score_list}

    print(student)

    #part c
    average_score = float(sum(score_list) / len(score_list))
    student.update({"average" : average_score})
    print(student)

    return 0

if __name__ == "__main__":
    sys.exit(main())