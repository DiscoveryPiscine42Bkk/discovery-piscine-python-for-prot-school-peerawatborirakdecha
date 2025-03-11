#!/usr/bin/python3

def main():
    """
    แก้ไขโปรแกรมก่อนหน้าเพื่อประมวลผลเฉพาะค่าที่มากกว่า 5 จากอาร์เรย์ต้นฉบับ
    """

    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []

    # วนซ้ำอาร์เรย์ต้นฉบับและประมวลผลเฉพาะค่าที่มากกว่า 5
    for value in original_array:
        if value > 5:
            new_value = value + 2
            new_array.append(new_value)

    # แสดงอาร์เรย์ทั้งสอง
    print(original_array)
    print(new_array)

if __name__ == "__main__":
    main()  