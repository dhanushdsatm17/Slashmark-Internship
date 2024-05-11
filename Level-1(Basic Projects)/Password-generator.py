import random
import string

def generate_password(length):
    passwords = []
    for _ in range(length):
        password = ""
        for _ in range(random.randint(3, 10)):  # Randomize password length between 3 to 10 characters
            password += random.choice(string.ascii_lowercase)
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    return passwords

def replace_with_number(password):
    replace_index = random.randrange(len(password) // 2)
    password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    replace_index = random.randrange(len(password) // 2, len(password))
    password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")

    passwords = []
    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        passwords.extend(generate_password(length))
    
    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i}: {password}")

if __name__ == "__main__":
    main()
