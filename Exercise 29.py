"""
Ask the user for:
their name (string)
their age (integer)
their country (string)
Store the results in a list 'profile = [name, age, country]'.

Then produce a new list:
'summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]'.

Finally print both lists with clear labels.
"""

import sys

def main():

    #ask user for name, age, country
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    country = input("What is your country of origin: ")

    profile = [name, age, country]
    summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]

    print("Input information: ", profile)
    print("Formatted information: ", summary)
    return 0

if __name__ == "__main__":
    sys.exit(main())