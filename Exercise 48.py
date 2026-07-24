"""
Ask the user for a value using input().

If the input is empty, print "No input provided".

Else if the input is numeric, print "Numeric input".

Else print "Text input".

Constraints:
No loops
No exception handling
Use:
.isdigit()
truthiness of strings
if / elif / else
"""

import sys

def main():

    #Ask the user for a value using input().
    user_input = input("Enter an input: ")

    #used not as if you put nothing it would be false thus not makes it true
    if not user_input:
        print("No input provided")
    elif user_input.isdigit():
        print("Numeric input")
    else:
        print("Text input")


    return 0

if __name__ == "__main__":
    sys.exit(main())