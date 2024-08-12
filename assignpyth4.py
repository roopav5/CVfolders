# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:21:03 2024

@author: Admin
"""

# Initialize an empty dictionary
dict1 = {}

# Open and read the file line by line
with open(r'C:\Users\Admin\Desktop\data1.txt', 'r') as file:
    line_number = 1
    for line in file:
        # Strip any leading/trailing whitespace and split by commas
        line = line.strip()
        numbers = line.split(',')
        
        # Convert each number to an integer
        numbers = [int(num) for num in numbers if num.isdigit()]
        
        # Create dictionary key and value
        key = f"Line-{line_number}"
        dict1[key] = numbers
        
        line_number += 1

# Process the dictionary
for key, values in dict1.items():
    if values:
        total_sum = sum(values)
        maximum = max(values)
        minimum = min(values)
    else:
        total_sum = maximum = minimum = average = 0
    
    # Print the results for the current line
    print(f"{key} - Sum: {total_sum}, Max: {maximum}, Min: {minimum}, Avg: {average}")
