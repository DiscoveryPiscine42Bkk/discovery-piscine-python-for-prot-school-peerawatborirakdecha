#!/usr/bin/python3
import sys

def main():
    """
    แสดงพารามิเตอร์สตริงแรกที่ส่งไปยังโปรแกรม
    ถ้าไม่มีพารามิเตอร์ ให้แสดง 'none'
    """

    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

if __name__ == "__main__":
    main()