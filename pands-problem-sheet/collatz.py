# Week Task 4 
# Author: Agnieszka Waszczuk 
# Reference https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e
#           https://stackoverflow.com/questions/61789065/automate-the-boring-stuff-with-python-collatz-sequence
#           https://github.com/thomaskellough/Automate-The-Boring-Stuff/blob/master/Practice-Projects/Ch%2003%20-%20Collatz%20Sequence.py
# 
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one
# Program end if the current value is one.

'''
Add input, positive number
'''
your_number = int(input('Please give me a positive number: '))

# check if the number is positive
# use <=0 , if number is less or 0 loop will back and request once again to add positive number 
# while loop is checking if the number is posivitve

while your_number <= 0:
    print(f'your number is {your_number} but need to be positve')
    your_number = int(input('Please give me a postive number: '))
print(f'your number is {your_number} and is positive')

# create empty list for the values
score = []
#if it is even, divide it by two, but if it is odd, multiply it by three and add one

while your_number !=1:
    if your_number%2 == 0:
        your_number = your_number/2
        score.append(your_number)
        #print(int(your_number))
    else:
        your_number = your_number*3+1
        #print(int(your_number))
        score.append(your_number)


print([int(x) for x in score])