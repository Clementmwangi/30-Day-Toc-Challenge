"""
Given:

rates = {
    "USD": 160.0,
    "EUR": 170.0,
    "GBP": 200.0

}

Ask the user for a currency code.

If the code exists in the dictionary, print the rate.

Otherwise, print "Currency not supported".
"""

import sys

def main():

    rates = {"USD": 160.0,
             "EUR": 170.0,
             "GBP": 200.0}

    #Ask the user for a currency code.
    user_code = input("Enter a currency code: ").upper()

    #use is not as we want to check the key not just the value
    if rates.get(user_code) is not None:
        print(f"The currency rate for e{user_code} is {rates[user_code]}")
    else:
        print("Currency not supported")


    return 0

if __name__ == "__main__":
    sys.exit(main())