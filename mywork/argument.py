# Weelky Task 7 
# Author : Agnieszka Waszczuk 
# Write a program that reads in a text file and outputs the number of e's it contains
# $ python es.py moby-dick.txt
# 116960



# Open file name 
FILENAME = "moby-dick.txt"

with open(FILENAME, 'r') as f:
    for data in f:
        print (data)
    