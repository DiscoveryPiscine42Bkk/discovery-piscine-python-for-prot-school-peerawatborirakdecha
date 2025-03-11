#!/usr/bin/python3

import sys
import re

def scan_it(keyword, string):
    """
    นับจำนวนครั้งที่ keyword ปรากฏใน string
    """
    if not keyword or not string:
        return 0
    
    matches = re.findall(re.escape(keyword), string)
    return len(matches)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("none")
    else:
        keyword = sys.argv[1]
        string = sys.argv[2]
        count = scan_it(keyword, string)
        if count > 0:
            print(count)
        else:
            print("none")