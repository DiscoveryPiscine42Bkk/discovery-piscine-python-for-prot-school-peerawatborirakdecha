#!/usr/bin/python3

import sys

def shrink(text):
    """
    แสดงตัวอักษร 8 ตัวแรกของสตริง
    """
    print(text[:8])

def enlarge(text):
    """
    ต่อท้าย 'Z' จนกว่าสตริงจะมีความยาว 8 ตัวอักษร
    """
    while len(text) < 8:
        text += 'Z'
    print(text)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        else:
            enlarge(arg)