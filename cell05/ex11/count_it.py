#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("none")
    else:
        num_params = len(sys.argv) - 1
        print(f"parameters: {num_params}")
        for i in range(1, len(sys.argv)):
            param = sys.argv[i]
            print(f"{param}: {len(param)}")
            ./count_it.py "Game" "of" "Thrones"