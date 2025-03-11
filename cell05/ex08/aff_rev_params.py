#!/usr/bin/python3

import sys

def aff_rev_params(args):
    """
    แสดงสตริงที่ส่งผ่านเป็นพารามิเตอร์ในลำดับย้อนกลับ
    """
    if len(args) < 2:
        print("none")
    else:
        for arg in reversed(args[1:]):
            print(arg)

if __name__ == "__main__":
    aff_rev_params(sys.argv)