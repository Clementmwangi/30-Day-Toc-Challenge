"""
Using the dictionary from the previous exercise, print:

the person's name
the person's age
"""

import sys

def main():

    person = {"name" : "Alice",
              "age" : 25,
              "country" : "Kenya"}
    
    print(f"Name: {person.get("name")}")
    print(f"Age: {person.get("age")}")
    return 0

if __name__ == "__main__":
    sys.exit(main())