# -*- coding: utf-8 -*-
"""
@author: Rohit Chavan
"""

with open('C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt') as f:
    contents = f.read()
print(contents)

'''rstrip() method remove or strips any whitespace'''
with open('C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt') as f:
    contents = f.read()
print(contents.rstrip())

# Read line by line code
filename = 'C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt'
with open(filename) as f:
    for line in f:
        print(line)
        
filename = 'C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt'
with open(filename) as f:
    for line in f:
        print(line.rstrip())
        
filename = 'C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt'
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
    
# Write in file
filename = 'C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt'
with open(filename, 'w') as f:
    f.write("Hii, I love Programming")
    
filename = 'C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt'
with open(filename, 'w') as f:
    f.write("Hii, I love Programming \n")
    f.write("I love creating new games")
    
# Appending to a file
filename = 'C:/Machine_Learning_Nowwww/new rohit data science/Basic/pi_digits.txt'
with open(filename, 'a') as f:
    f.write("\nI also love finding meaning")