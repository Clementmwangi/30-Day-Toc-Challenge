"""
Given "items = [10, 20, 30]", crate an independent copy using slicing and print both lists.
"""

import sys

def main():

    items =[10, 20, 30]
    items2 = items[:]

    print("items:", items)
    print("items2:", items2)

    return 0

if __name__ == "__main__":
    sys.exit(main())