import random
import string

print("--- Password Generator ---")

length = int(input("Enter password length: "))

use_digits = input("Include digits? (a/A): ").lower() == 'a'
use_symbols = input("Include symbols? (a/A): ").lower() == 'a'

characters = string.ascii_letters

if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)