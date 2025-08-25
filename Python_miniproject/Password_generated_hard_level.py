# HARD_LEVEL generated Password put order shuffle EX: 49o*(12(&11haWA

import random
import string

Password_Generated = []
print("\tWelcome to the PASSWORD GENERATED")

letters = int(input("How many letters would you like in your password? "))
for i in range(letters):
    Password_Generated.append(random.choice(string.ascii_uppercase + string.ascii_lowercase))

symbols = int(input("How many Symbols would you like? "))
for i in range(symbols):
    Password_Generated.append(random.choice(string.punctuation))

numbers = int(input("How many Numbers would you like? "))
for i in range(numbers):
    Password_Generated.append(random.choice(string.digits))

random.shuffle(Password_Generated)
Password = ''

for i in Password_Generated:
    Password += i

print(f'Your Hard level Password: {Password}')