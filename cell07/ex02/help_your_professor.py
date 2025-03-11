#!/usr/bin/python3

def average(student_scores):
    """
    คำนวณค่าเฉลี่ยคะแนนของนักเรียนจากพจนานุกรม
    """
    total_score = sum(student_scores.values())
    return total_score / len(student_scores)

if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")