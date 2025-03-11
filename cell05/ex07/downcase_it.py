import sys

def downcase_it(input_string):
    """
    แปลงสตริงที่กำหนดให้เป็นตัวพิมพ์เล็กและพิมพ์ออก
    หากจำนวนพารามิเตอร์ไม่ถูกต้อง พิมพ์ 'none'
    """
    if len(sys.argv) != 2:
        print("none")
    else:
        print(input_string.lower())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        downcase_it(input_string)
    else:
        downcase_it("")  # เรียกใช้ฟังก์ชันโดยไม่มีอินพุต