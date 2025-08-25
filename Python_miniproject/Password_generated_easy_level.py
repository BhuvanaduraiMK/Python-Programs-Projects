# generated Password put order not shuffle EX: first ALPHAPET, Second SYMBOLS, Third NUMBERS

import random
import string

Password_Generated = ''
print("\tWelcome to the PASSWORD GENERATED")

letters = int(input("How many letters would you like in your password? "))
for i in range(letters):
    Password_Generated += random.choice(string.ascii_uppercase + string.ascii_lowercase)

symbols = int(input("How many Symbols would you like? "))
for i in range(symbols):
    Password_Generated += random.choice(string.punctuation)

numbers = int(input("How many Numbers would you like? "))
for i in range(numbers):
    Password_Generated += random.choice(string.digits)

print(f'Your Easy level Password: {Password_Generated}')