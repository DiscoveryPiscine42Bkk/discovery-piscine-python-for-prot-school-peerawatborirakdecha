#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in sys.argv[1:]:
            if arg.endswith("ism"):
                continue  # ข้ามถ้าลงท้ายด้วย "ism"
            print(arg + "ism")