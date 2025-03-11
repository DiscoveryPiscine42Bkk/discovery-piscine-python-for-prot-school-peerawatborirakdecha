#!/usr/bin/python3

def add_one(num):
    """
    เพิ่ม 1 ให้กับตัวเลขที่ส่งเข้ามา
    """
    num += 1
    print(f"ภายในฟังก์ชัน add_one: num = {num}")  # เพิ่มบรรทัดนี้เพื่อแสดงค่า num ภายในฟังก์ชัน

    return num

if __name__ == "__main__":
    my_num = 5
    print(f"ก่อนเรียกใช้ฟังก์ชัน: my_num = {my_num}")

    add_one(my_num)

    print(f"หลังเรียกใช้ฟังก์ชัน: my_num = {my_num}")