#!/usr/bin/python3

def famous_births(person_dict):
    """
    จัดเรียงและแสดงข้อมูลบุคคลตามวันเกิด
    """
    sorted_persons = sorted(person_dict.items(), key=lambda item: item[1]["date_of_birth"])
    for key, value in sorted_persons:
        name = value["name"]
        birth_date = value["date_of_birth"]
        print(f"{name} is a great scientist born in {birth_date}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
    }
    famous_births(women_scientists)