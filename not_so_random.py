import random
import string


def generate_password(minimum_length, numbers=True, special_characters=True):
    minimum_length = max(minimum_length, 2)
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    special = ["!", "@", "#", "$", "%", "^", "&", "*"]

    password = random.choice(upper_letters)

    for _ in range(0, 3):
        password += random.choice(lower_letters)

    for _ in range(0, 4):
        password += random.choice(digits)

    password += random.choice(special)

    return password


minimum_length = int(input("Enter the minimum length: "))
has_digit = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
password = generate_password(minimum_length, has_digit, has_special)
print(password)
