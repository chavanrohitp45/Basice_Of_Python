# -*- coding: utf-8 -*-
"""
@author: Rohit Chavan
"""
# Print 
print('Hello World!')

# Variables
x = 1
print(x)
print(type(x))

x = 100.0
print(x)
print(type(x))

# Floating point numbers
exchange_rate = 1.90
print(exchange_rate)
print(type(exchange_rate))

# Take input from user
age = input("Enter your Age: ")
print(type(age))
print(age)

age1 = int(input("please enter age"))
print(type(age1))
print(age1)
age2 = int(input("please enter age"))
print(type(age2))
print(age2)
age = age1+age2
print(age)

# Complex number
c1 = 1
c2 = 2j
print('c1:', c1, 'c2:', c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

# Boolean value
all_ok = True
print(all_ok)
print(type(all_ok))

# Convert string into boolean
status = bool(input("ok it is confirmed!!"))
print(status)
print(type(status))

# Arithmetic Operations
n1 = 10
n2 = 5
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(type(n1 + n2))
print(10 * 4)
print(type(10*4))

home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

print(100 /20)
print(type(100/ 20))
print(100 // 20)
print(type(100 // 20))
print('Modulus division 100 % 13:', 100 % 13)
print('Modulus division 3 % 2:', 3 % 2)

a =  5
b = 3
print(a**b)

x = 0
x += 1
print(x)

# Positive or Negative Numbers
n = int(input("Enter a number: "))
if n < 0:
    print("Negative number")
else:
    print("positive number")
    
# elif statements
saving = float(input("Enter your saving: "))
if saving == 0:
    print("No Saving")
elif saving < 500:
    print('Well Done')
elif saving < 1000:
    print("thats a tidy sum")
elif saving < 10000:
    print("welcome sir!!")
else:
    print("thank you")
    
# Break loop statements
num = int(input("enter the number"))
for i in range(0,6):
    if i == num:
        break
    print(i, ' ', end='')
print("done!!")

for i in range(0, 10):
   #print(i, ' ', end='')
    if i % 2 == 1:
     continue
     print('hey its an even number')
     print('we love even numbers')
print('Done')

# Float value
int_val = 100
string_val = '1.5'
float_val = float(int_val)
print("int to float: ", float_val)
print(type(float_val))
float_val = float(string_val)
print("String to float: ", float_val)
print(type(float_val))

# Nested if elif
print("Welcome to the roller coaster")
height=int(input("Please enter your height"))

if height>=120:
    print("you can ride the roller coaster")
    age=int(input("Please enter your age "))
    if age<12:
        print("your ticket will be 5$")
    elif age>12 and age<18:
        print("your ticket will be 7$")

    elif age>18:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")     
 
# Nested if-else
print("Welcome to the roller coaster")
height=int(input("Please enter your height"))
age=int(input("Please enter your age "))
if height>=120:
    print("you can ride the roller coaster")
    if age<=18:
        print("your ticket will be 7$")
    else:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")    

# is and is not operator
winner  = None
print(winner is None)
print(winner is not None)

winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True

# Comparison Operator
n = int(input('enter a number'))
if n > 0:
    print(n)

# while loop
count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1
          
# For Loop
print('Print out values in a range')
for i in range(2,10):
   print(i)
   print('Done') 
    
# Anonymous loop variable
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 16):
    if i == num:
      break
    print(i)
    print('Done')
    
for _ in range(0,10):
    print('.', end='')
    print()
    
    