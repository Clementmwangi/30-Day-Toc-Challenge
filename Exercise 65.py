"""
Introducing the while-construct
If you have noticed, the for-construct is used whenever it is clear how many iterations are required. 
This makes it a determinate looping construct. However, there are many cases where the number of 
iterations is indeterminate. For this we need a new looping construct that blends the assignment 
expressions we encountered in if-constructs and the looping property of the for-construct: the 
while-construct. Here is the skeleton of a while-construct:

while <assignment_expression>:
    # suite

Within the suite must exist an expression that modifiers some variable that is part of the assignment
 expression. Run the following example to determine what it outputs.

i = 0
while i < 5:
    print(i)
    i += 1 # statement that modifies i

Over to you: Use a while loop to print numbers from 5 to 1 so that your program produces the 
following output:

5
4
3
2

1

Bonus question: What happens if the suite does not include a statement that modifies the variable
 in the assignment expression? Try it!
"""

import sys

def main():

    i = 5
    while i > 0:
        print("Hi")# runs infinitely
    
    return 0

if __name__ == "__main__":
    sys.exit(main())