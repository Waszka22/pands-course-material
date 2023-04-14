# Lab
# Week 03
# Write a program (div.py) that reads in two numbers and
#divides the first one by the second and give the integer result and the
#remainder.


# program that reads in two numbers 
# outputs the integer answer and remainder

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = x%y # % gives the remainder
print("{} divided by {} is {} with remainder {}".format( x, y,
answer, remainder))