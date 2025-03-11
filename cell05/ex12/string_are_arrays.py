#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("none")
    else:
        input_string = sys.argv[1]
        z_count = 0
        for char in input_string:
            if char == 'z':
                print('z', end='')  # พิมพ์ 'z' โดยไม่ขึ้นบรรทัดใหม่
                z_count += 1
        if z_count == 0:
            print("none")
        else:
            print()  # ขึ้นบรรทัดใหม่หลังพิมพ์ 'z' ทั้งหมด