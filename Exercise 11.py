"""
Ask the user for a number representing minutes. Convert to hours (float) and print:

"You entered X minutes which is Y hours."
"""

import sys

def main():
    #ask user for input
    minutes = int(input("Enter a number to represent minutes: "))
    hours = minutes / 60 

    print(f"You entered {minutes} minutes which is {hours: .2f} hours")
    return 0
    

if __name__ == "__main__":
    sys.exit(main())
