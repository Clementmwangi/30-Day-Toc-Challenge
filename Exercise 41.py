"""
Ask the user for:
name
birth year (integer)
country
Store them in a dictionary profile.

Then create a new dictionary summary with:
"NAME" → uppercase name
"age_in_2025" → 2025 - birth_year
"country" → lowercase country
Print both dictionaries with labels.
"""

import sys

def main():

    #ask user for info and store in a dictionary
    user_name = input("Enter your name: ")
    birth_year = int(input("Enter your year of birth: "))
    user_country = input("Enter the country of residence: ")

    user_data = {"name" : user_name,
                 "year" : birth_year,
                 "country" : user_country}

    updated_data = {"name" : user_name.upper(),
                    "age_in_2025" : (2025 - birth_year),
                    "country" : user_country.lower()}

    print("Original information: ", user_data)

    print("Current data:", updated_data)

    return 0

if __name__ == "__main__":
    sys.exit(main())