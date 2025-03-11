#!/usr/bin/env python3

# round_up.py

import math

num_str = input("Give me a number: ")

try:
    num = float(num_str)
    rounded_num = math.ceil(num)
    print(rounded_num)
except ValueError:
    print("Invalid input: Please enter a valid number.")