"""
Ask the user for:
a username
a boolean flag "is_admin" (True/False)
Given:

access_level = 1

If the user is "admin" or is_admin is True, increase access_level by 4.
"""

import sys

def main():

    #Ask the user
    user_name = input("Enter a username: ")
    is_admin = input("Are you an admin(Enter True or False): ").capitalize() == "True"

    access_level = 1

    #didn't use bool as it would still be true as long as the string isn't empty.
    if is_admin:
        access_level += 4
        print(f"{user_name} your access_level has been increased to {access_level } ")
    else:
        print(f"{user_name} your access_level is {access_level} ")

    return 0

if __name__ == "__main__":
    sys.exit(main())