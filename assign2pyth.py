"""
Created on Sun Aug  4 23:16:27 2024

@author: Admin
"""

# Data to append
v1 = "10,13,22,65,28"
v2 = "43,199,501"

# Open the file in append mode
with open(r'C:\Users\Admin\Desktop\data1.txt', 'a') as file_handle:
    file_handle.write(v1 + '\n')
    file_handle.write(v2 + '\n')
