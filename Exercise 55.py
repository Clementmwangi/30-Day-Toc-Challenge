"""
Ask the user for:
name
three test scores (integers)
Store the data in a dictionary:

student = {
    "name": ...,
    "scores": [...],

}

Compute the average score and add it to the dictionary.

Then:
If the average is ≥ 70, status is "Pass"
If the average is ≥ 50 and < 70, status is "Supplementary"
Otherwise, status is "Fail"
Add "status" to the dictionary and print the final record neatly.

Constraints:
Must use if / elif / else
Must use and
Must use compound assignment at least once
Must reuse Week 1-3 ideas (lists, dicts, arithmetic)
"""

import sys

def main():

    #Ask the user
    user_name = input("Enter your name: ").capitalize()
    score1 = int(input("Enter your first score: "))
    score2 = int(input("Enter your second score: "))
    score3 = int(input("Enter your third score: "))

    student = {"name" : user_name,
               "scores" : [score1, score2, score3]}

    average_score = int(sum(student.get("scores")) / len(student.get("scores")))

    student["average_score"] = average_score

    if student.get("average_score") >= 70:
        status = "Pass"
    elif 50 <= student.get("average_score") < 70:
        status = "Supplementary"
    else:
        status = "Fail"

    student["status"] = status

    for key, value in student.items():
        print(f"{key} : {value}")
    
    

    return 0

if __name__ == "__main__":
    sys.exit(main())