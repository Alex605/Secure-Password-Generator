import random

length = input('How many characters would you like in your password?: ')
length = int(length)

choice = input('Enter \'1\' for just letters and numbers, or type \'2\' to also include special characters. ')
choice = int(choice)

if choice == 1:
  chars = 'ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuvwxyz1234567890'

elif choice == 2:
  chars = 'ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuvwxyz1234567890!#$%&()*+,-./<=>?@[]\^_`{|}~'

else:
  print("Invalid Choice");
  
password = ''

for c in range(length):
  password += random.choice(chars)
  
print(password)