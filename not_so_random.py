import random
import string


def generate_password():
    password_set = set()  # Update after conditionals
    newpword_set = set()  # Update after conditionals

    # String ASCII & Digit + custom string_speci Variables
    string_upper = string.ascii_uppercase
    string_lower = string.ascii_lowercase
    string_digit = string.digits
    string_speci = ["!", "@", "#", "$", "%", "^", "&", "*"]

    # Random Choice Variables
    upper_chars = random.choice(string_upper)
    speci_chars = random.choice(string_speci)
    lower_chars = ""  # Update on conditional
    numbr_chars = ""  # Update on conditional
    randm_passw = ""  # Update on conditional

    # Conditionals for lower_chars, numbr_chars, randm_passw
    for _ in range(0, 3):
        lower_chars += random.choice(string_lower)
    for _ in range(0, 4):
        numbr_chars += random.choice(string_digit)

    # Saving generated values, separated in a Tupple
    password_set.add = (upper_chars, speci_chars, lower_chars, numbr_chars)

    for _ in range(0, len(password_set)):
        while len(newpword_set) != len(password_set):
            newpword_set.update(password_set[_])

    # if isinstance(passw_list[0], str):
    #     randm_passw = random.choice(passw_list)

    print(newpword_set)
    return newpword_set


generate_password()
