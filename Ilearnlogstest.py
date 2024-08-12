# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:23:35 2024

@author: Admin
"""

import pandas as pd
import os

# Load the Excel_File :
data = pd.read_excel('C:\\Users\\Admin\\Desktop\\Ilearnlogs.xlsx')
df = pd.DataFrame(data)

#Extract course and chapter :
course = []
chapters = []

for path in df['path'] :
    parts = path.strip('/').split('/')
    if len(parts) >=3:
        course.append(parts[1])
        chapters.append(parts[2])
    else:
        course.append(None)
        chapters.append(None)

# Adding course & chapters into Dataframe:
df['course'] = course
df['chapters'] = chapters

# Records without chapters :
Records_1 = df[df['chapters'].isnull()]

# Removing the records :
Removing = df[df['chapters'].notnull()]

#Save the filter_DataFrame :
Filtered_file_path = ('C:\\Users\\Admin\\Desktop\\Ilearnlogs_1.xlsx')
Removing.to_excel(Filtered_file_path, index = False)

print(f'Filtered Data saved to {Filtered_file_path}')