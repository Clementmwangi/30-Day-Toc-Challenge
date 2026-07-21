import sys

def main():
    #ask for user input 
    name = input("What is your name: ")

    #print user name
    print(f"Hello, {name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())