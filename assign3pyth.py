# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:18:11 2024

@author: Admin
"""

# 1. Append data from the set `st1` to `data1.txt`

st1 = {-17, 188, -2, -68, 162, 204, -151, -197, -86, 102}

with open(r'C:\Users\Admin\Desktop\data1.txt', 'a') as file_handle:
    # Convert each element to string and join with commas
    st1_str = ','.join(map(str, st1))
    file_handle.write(st1_str + '\n')

# 2. Compute sum and average for positive numbers only

lst = []

with open(r'C:\Users\Admin\Desktop\data1.txt', 'r') as file:
    for line in file:
        # Strip any leading/trailing whitespace and split by commas
        line = line.strip()
        numbers = line.split(',')
        
        # Convert each number to an integer and append to the list if positive
        for num in numbers:
            try:
                number = int(num)
                if number > 0:
                    lst.append(number)
            except ValueError:
                # Handle any non-numeric data gracefully
                pass

# Calculate the sum and average of positive numbers
total_sum = sum(lst)
average = total_sum / len(lst) if lst else 0

# Print the results
print("List of positive numbers:", lst)
print("Sum of positive numbers:", total_sum)
print("Average of positive numbers:",average)

# 3. Append data from the set `s2` to `data1.txt`

s2 = {'A72', 'B890', 'C1234', 'D-21', 'E75', 'F321'}

with open(r'C:\Users\Admin\Desktop\data1.txt', 'a') as file_handle:
    # Extract numbers from each string, ignoring the first character
    s2_numbers = [item[1:] for item in s2 if item[1:].isdigit()]
    # Join numbers with commas
    file_handle.write(s2_str + '\n')
