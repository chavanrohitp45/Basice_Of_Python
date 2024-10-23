# -*- coding: utf-8 -*-
"""
@author: Rohit Chavan
"""

"""
Exceptions are the issues that appear on run time.

Exception are handled with try-except block.
"""

# Handeling the ZeroDivisionError exception
print(5/0)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
    
# Handeling the FileNotFoundError Exception

filename = 'alice.txt'
with open(filaname, encoding='utf-8') as f:
    content = f.read()
    
filename = 'a.txt'
with open(filename, encoding = 'utf-8') as f:
    content = f.read()
    
filename = 'alice.txt';
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"sorry, the file{filename} does not exist")
   
filename ='a.txt'
try:
    with open(filename,encoding = 'utf-8') as f:
        content = f.read()
except  FileNotFoundError:
    print(f"sorry,the file{filename} does not exist")