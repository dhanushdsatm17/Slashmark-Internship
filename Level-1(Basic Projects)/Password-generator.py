"""This Python script generates strong, random passwords that include a mix of lowercase letters, numbers, and uppercase letters.

Features:

1.Customizable Length: Specify the desired length for each generated password.
2.Random Length Variation: Passwords can have a random length between 3 and 10 characters for added security.
3.Number and Uppercase Inclusion: Ensures each password contains at least one number and one uppercase letter.
4.Multiple Password Generation: Generate multiple passwords at once to suit your needs.

Getting Started:

*Save the code: Create a Python file (e.g., secure_password_generator.py) and paste the code into it.
*Run the script: Open a terminal or command prompt, navigate to the directory containing secure_password_generator.py, and execute python secure_password_generator.py.

Security Note:

1.It is recommended to store passwords securely using a password manager.
2.Do not share generated passwords with anyone."""

import random
import string

def generate_password(lengths):
    passwords = []
    for length in lengths:
        password = ''.join(random.choices(string.ascii_lowercase, k=length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    return passwords

def replace_with_number(password):
    for _ in range(random.randint(1, 2)):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    for _ in range(random.randint(1, 2)):
        replace_index = random.randrange(len(password) // 2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")

    passwords_lengths = []
    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        passwords_lengths.append(max(3, length))
    
    passwords = generate_password(passwords_lengths)

    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i}: {password}")

if __name__ == "__main__":
    main()
