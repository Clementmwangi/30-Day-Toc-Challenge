"""
Using the same dictionary from Exercise 60, print each value.
"""

import sys

def main():

    person = {"name": "Alice", "age": 30, "city": "Nairobi"}
    
    for individual in person.values():
        print(individual)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())