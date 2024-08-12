# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:14:50 2024

@author: Admin
"""

import os

print("Current Working Directory:", os.getcwd())

# Replace with your file path
file_path = r'C:\Users\Admin\Desktop\data1.txt'

# Check if the file exists
if os.path.isfile(file_path):
    lst = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            numbers = line.split(',')
            for num in numbers:
                lst.append(int(num))
    
    total_sum = sum(lst)
    average = total_sum / len(lst) if lst else 0
    
    print("List of numbers:", lst)
    print("Sum:",total_sum)
    print("Average:", average)
else:
    print("File not found: ",file_path)
