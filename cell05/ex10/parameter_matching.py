#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("none")
    else:
        parameter = sys.argv[1]
        user_input = input("What was the parameter? ")
        if user_input == parameter:
            print("Good job!")
        else:
            print("Nope, sorry...")