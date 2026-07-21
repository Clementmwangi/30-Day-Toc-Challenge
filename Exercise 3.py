"""
Ask the user for a float representing temperature in °C. Print the temperature in °F using:

F = C * 9/5 + 32
"""
import sys


def main():
    #ask user for a float
    userF = float(input("Enter temperature in celsius with decimal places: "))

    fahrenHeit = userF * 9 / 5 + 32

    print(f"The temperature in fahrenheit is {fahrenHeit}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

