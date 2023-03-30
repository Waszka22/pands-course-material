#Weekly task 6
# Author Agnieszka Waszczuk
#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
#This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).
#I suggest that you look at the newton method at estimating square roots.
#This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

# import the math modue
import math

# Request enter positive number 
positive_number = float(input('Please enter a positive number: '))

# The number is less than 0, request add once again
# The 78number is positive 
while positive_number <0 :
    print("Your number is negative, try again! ")
    positive_number = float (input('Please enter a positive number: '))
# Return the square root
result = math.sqrt(float(positive_number))
print(f'The square root of {positive_number} is : {result}')
