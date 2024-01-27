import random
import string


def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    chars = letters

    if numbers:
        chars += digits
    if special:
        chars += special

    password = ""
    meets_criteria = False
    has_digit = False
    has_special = False

    while not meets_criteria or len(password) < minimum_length:
        new_chars = random.choice(chars)
        password += new_chars

        if new_chars in digits:
            has_digit = True
        elif new_chars in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_digit
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password


minimum_length = int(input("Enter the minimum length: "))
has_digit = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
password = generate_password(minimum_length, has_digit, has_special)
print(password)
