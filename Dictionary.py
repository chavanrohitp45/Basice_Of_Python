# -*- coding: utf-8 -*-
"""
@author: Rohit Chavan
"""
# Create a Dictionary
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
print(capitals)

# Accessing the Dictionary
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
print('Capitals[Maharashtra]: ', capitals['Maharashtra'])

# Adding elements
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
capitals['West_Bengal']="Kolkata"
capitals

# Change key value
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
capitals['Gujrat'] = 'Gandhinagar'
capitals

# Remove elements
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
capitals.pop('Karnataka')
capitals
del capitals['Gujrat']
capitals

# Iterating over keys
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
for states in capitals:
    print(states, end= " , ")

for states in capitals:
    print(states, end= ' , ')
    print(capitals[states])
    
# Values, Keys and Items
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
print(capitals.values())
print(capitals.keys())
print(capitals.items())

# Membership Operator (in / not in)
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
print('Karnataka' in capitals)
print('Bihar' not in capitals)
print('Bihar' in capitals)

# Length (len)
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahemadabad',
    'Karnataka': 'Banglore',
    'Andrapradesh': 'Hyderabad'
    }
print(len(capitals))

# Dictionary can have value in tuple
seasons = {
    'summer': ('feb', 'mar', 'apr', 'may'),
    'rainy':('june','july','august','sept'),
    'winter':('oct','nov','december','january')  
    }
print(seasons['rainy'])
print(seasons['rainy'][1])
print(seasons['summer'][2])
print(seasons['winter'][2:])

# Dictionaries cannot have two items with the key
dict2={
       'brand':'maruti',
       'model':'breeza',
       'year':2021,
       'year':2020
       }
print(dict2)

# Loop
dict2={
       'brand':'maruti',
       'model':'breeza',
       'year':2020
       }

for x in dict2:
    print(x)
    
    
for x in dict2:
    print(dict2[x])


for x in dict2.values():
    print(x)

    
for x in dict2.keys():
    print(x)


for x,y in dict2.items():
    print(x,y)
    
# Copy a Dictionary
dict2={
       'brand':'maruti',
       'model':'breeza',
       'year':2020
       }
mydict =dict2.copy()
print(mydict)

# Unpacking of dictionary
friends={
    "Dale":9850,
    "male":6032
    }

contacts={
    "dada":8530,
    "mama":5286
    }

contacts.update(friends)
print(contacts)

# pipe operator
friends={
        "Satish":99021,
         "Ram":97603
         }
sham={"sham":85305}
all_friends = friends | sham
print(all_friends)
