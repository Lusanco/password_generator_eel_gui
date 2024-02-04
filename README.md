# Password Generator Eel GUI (WIP)

Project and README.md under construction.

This repository contains two Python scripts for generating random passwords: `not_so_rnd_gen.py` and `orig_passw_gen.py`. Also, it will have a Eel Graphical User Interface.

Below imported non GUI scripts description. 

## not_so_rnd_gen.py

This script generates a random password with a combination of uppercase letters, special characters, lowercase letters, and digits. It includes the following steps:

1. Define character sets for uppercase letters, lowercase letters, digits, and special characters.
2. Randomly choose one character from the uppercase set and one from the special character set.
3. Use conditionals to generate three lowercase characters and four digit characters.
4. Save the generated characters in a set (`password_set`) and then convert them into a list (`password_list`).
5. Concatenate the characters in the list to form the final password (`randm_passw`).
6. Print the generated password for the user.

To run the script, execute the following command:

```bash
python not_so_rnd_gen.py
```

## orig_passw_gen.py

This script provides a more customizable password generation approach. It takes user input for the minimum length of the password and whether to include numbers and special characters. The steps include:

1. Define character sets for uppercase letters, lowercase letters, digits, and special characters.
2. Concatenate the character sets based on user input regarding numbers and special characters.
3. Use a while loop to generate a password until it meets the specified criteria.
4. Prompt the user for the minimum length, whether to include numbers, and whether to include special characters.
5. Generate and print the password based on user input.

To run the script, execute the following command:

```bash
python orig_passw_gen.py
```

## Usage

Choose the script that best fits your password generation needs. Execute the script in the terminal and follow the prompts to customize the generated password.

## Disclaimer

**Note:** I am not responsible for the use of these scripts. They are provided as-is, with no guarantee of their suitability for any specific purpose. Use them responsibly and at your own risk.