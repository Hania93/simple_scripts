import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")

num_of_numbers = int(input('How many numbers would you like to generate?'))
num_of_letters = int(input('How many letters would you like?'))
num_of_symbols = int(input('How many symbols would you like?'))

password_chars = []

for i in range(0, num_of_numbers):
    password_chars.append(random.choice(numbers))

for i in range(0, num_of_letters):
    password_chars.append(random.choice(letters))

for i in range(0, num_of_symbols):
    password_chars.append(random.choice(symbols))

random.shuffle(password_chars)

password = ''.join(password_chars)

print(f'Generated password is {password}')
