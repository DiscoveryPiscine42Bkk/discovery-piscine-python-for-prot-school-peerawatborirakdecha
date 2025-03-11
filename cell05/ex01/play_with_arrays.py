#!/usr/bin/python3

def main():
    """
    สร้างโปรแกรมที่สร้างอาร์เรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละค่าในอาร์เรย์ต้นฉบับ
    """

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []

    # วนซ้ำอาร์เรย์ต้นฉบับและเพิ่ม 2 ให้กับแต่ละค่า
    for value in original_array:
        new_value = value + 2
        new_array.append(new_value)

    # แสดงอาร์เรย์ทั้งสอง
    print("Original array:", original_array)
    print("New array:", new_array)

if __name__ == "__main__":
    main()