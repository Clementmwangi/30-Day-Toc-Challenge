"""
Call print() on a message and assign it to a variable:

v = print("Hello")

Print v and observe its value.

"""

import sys

def main():
    v = print("Hello i am clement")
    #it seems that v just executes the print and returns none 
    print(v) 
    return 0

if __name__ == "__main__":
    sys.exit(main())