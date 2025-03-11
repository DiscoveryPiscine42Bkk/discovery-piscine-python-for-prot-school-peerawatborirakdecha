#!/usr/bin/python3
import sys

def main():
    """
    แสดงสตริงที่ส่งเป็นพารามิเตอร์ในรูปแบบตัวพิมพ์ใหญ่
    ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 ให้แสดง 'none'
    """

    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        print(input_string.upper())
    else:
        print("none")

if __name__ == "__main__":
    main()