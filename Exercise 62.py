"""
Print:

key -> value

for each entry in the dictionary. For example, if the dictionary has the key-value pair "a" and 36 
your programme should print out:

a -> 36
"""

import sys

def main():

    original = {"product_id": 4829,
                "quantity_in_stock": 150,
                "items_sold": 34,
                "reorder_level": 10,}

    for key, value in original.items():
        print(f"{key} -> {value}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())