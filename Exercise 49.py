"""
Given:

colors = ["red", "green", "blue"]

Ask the user for a color.

If the color is in the list, print "Color available", else print "Color not found".
"""

import sys

def main():

    colors = ["red", "green", "blue"]

    user_color = input("Enter a random color: ").lower()

    #used in as it checks and returns true if a value is in a list without using a loop
    if user_color in colors:
        print("Colour available")
    else:
        print("Color not found")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())