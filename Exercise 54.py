"""
Ask the user for an optional middle name.

If the input is empty, set middle_name = None.

If middle_name is not None, print the full name with middle name.

Else print only first and last name.
"""

import sys

def main():

    #Ask the user for an optional middle name.
    user_first = input("Enter your first name: ")
    user_option = input("Enter your middle name(optional): ")
    user_last = input("Enter your last name: ")

    if user_option == "":
        user_option = None

    if user_option is not None:
        print(user_first + ' ' + user_option + ' ' + user_last)
        
    else:
        print(user_first + ' ' + user_last)


        


    return 0

if __name__ == "__main__":
    sys.exit(main())