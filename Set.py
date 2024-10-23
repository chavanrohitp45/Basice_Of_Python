# -*- coding: utf-8 -*-
"""
@author: Rohit Chavan
"""

# Create a set
basket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

#Accessing Elements
basket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for item in basket:
    print(item)
    
# Adding Elements
basket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket.add('apricot')
print(basket)

# Add more elements 
basket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapes'])
print(basket)

# Length
basket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(len(basket))

# max and min
basket2 = {23,45,45,56,34}
print(max(basket2))
print(min(basket2))

# Remove elements
basket= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
basket.remove('apple')
basket.discard('orange')
print(basket)

# Set Operations
s1 = {'apple','orange','pear','banana'}
s2 = {'apricot','mango','grapefruit','banana'}
print("Union: ", s1|s2)
print('Intersection: ', s1&s2)
print('Difference: ', s1-s2)
print('Difference: ', s2-s1)