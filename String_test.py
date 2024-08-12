# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:52:22 2024

@author: Admin
"""

#s1.translate(",")
#'abc;xyz;pqr'
translation_table = str.maketrans({
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'ring = "Hello, this is an example."

translated_string = original_string.translate(translation_table)
print(f"Original string: {original_string}")
#Original string: Hello, this is an example.
print(f"Translated string: {translated_string}")
