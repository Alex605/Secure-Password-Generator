#!/bin/python3
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuvwxyz1234567890!#$%&()*+,-./<=>?@[]\^_`{|}~'

length = input('How many characters would you like in your password?: ')
length = int(length)

password = ''

for c in range(length):
  password += random.choice(chars)
  
print(password)