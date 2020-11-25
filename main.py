import database
import random

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
password_2 = []
password_3 = []
final_password = []

for letters in database.letters:
    random_letters = random.randint(0, len(database.letters))
    if len(password) < nr_letters:
        password += database.letters[random_letters - 1]

for symbols in database.symbols:
    random_symbols = random.randint(0, len(database.symbols))
    if len(password_2) < nr_symbols:
        password_2 += database.symbols[random_symbols - 1]

for numbers in database.numbers:
    random_numbers = random.randint(0, len(database.numbers))
    if len(password_3) < nr_numbers:
        password_3 += database.numbers[random_numbers - 1]

final_password.extend(password + password_2 + password_3)

random.shuffle(final_password)
print(final_password)
