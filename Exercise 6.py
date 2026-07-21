"""
Give a variable x = 10.

Update it using +=, -=, *=, and **= (compute powers) and print each result.
"""

import sys

def main():
    x = 10

    x+=20
    print(f"when using += and adding 20 the result is {x}")

    x-=20
    print(f"when using -= and minusing 20 the result is {x}")

    x*=2
    print(f"when using *= and multiplying by 2 the result is {x}")

    x**=2
    print(f"when using ** and powering by 2 the result is {x}")

    return 0
    

if __name__ == "__main__":
    sys.exit(main())
