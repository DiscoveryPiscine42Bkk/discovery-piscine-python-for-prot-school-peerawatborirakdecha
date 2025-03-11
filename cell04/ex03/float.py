#!/usr/bin/env python3

# float.py

num_str = input("Give me a number: ")

if '.' in num_str:
    try:
        num = float(num_str)
        print("This number is a decimal.")
    except ValueError:
        print("Invalid input: Please enter a valid number.")
else:
    try:
        num = int(num_str)
        print("This number is an integer.")
    except ValueError:
        print("Invalid input: Please enter a valid number.")