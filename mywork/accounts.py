# Weekly Task 03
# Author : Agnieszka Waszczuk 
# Create variables for the input value and convert input
# Reference https://realpython.com/python-input-output/

# Request enter 10 digits account number 
account_no = input('Please enter an 10 digit account number:')

# Use loop to check if the user put the correct number of digits
# If no 10-digit request numbers have been entered, it will be prompted again 
while len (account_no) !=10:
    print(f'\nYou entered {len(account_no)} digits. You need to enter 10 digits') 
    print('Plase try again')
    account_no = input ('Plase enter an 10 digits account number: ')

 # Create a string with 6xXs and last for digits from account number 
 # Using [-4] shows only last 4 account digits 
account_no_hidden = f'XXXXXX{account_no[-4:]}'
print(account_no_hidden)

