# -*- coding: utf-8 -*-
"""
@author: Rohit Chavan
"""

# Creating tuple
tup1 = (1,2,3,4)
print(tup1)

# Accessing elements
print(f'tup1[0]:{tup1[0]}')
print(f'tup1[1]:{tup1[1]}')
print(f'tup1[2]:{tup1[2]}')
print(f'tup1[3]:{tup1[3]}')

# Tuples can hold different data types
tup2 = (1, 'john', True, 45.66)
for i in tup2:
    print(i)
    print(type(i))
    
# Used range function
tup3 = ('apple', 'orange', 'plum','apple')
for i in range(0,4):
    print(tup3[i])
    
# length
len(tup3)

# count how mant times a specified value is there
tup4 = ('apple', 'orange', 'plum', 'apple','banana')
print(tup4.count('apple'))

# index
print(tup4.index('apple'))

# Check if element is exist or not
tup4 = ('apple', 'orange', 'plum', 'apple','banana')
if 'banana' in tup4:
    print('Yesss!!!!')
else:
    print("Not!!!!")
    
# Nested Tuples
tup1 = (1,2,3,4)
tup2 = ('john', 'denise')
tup3 = (tup1, tup2)
print(tup3)