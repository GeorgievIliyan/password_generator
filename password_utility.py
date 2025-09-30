import random
import string
import pyperclip

def generate_password(length: int, has_digits: bool, has_uppercase: bool, has_symbols: bool ) -> str:
    chars = list(string.ascii_lowercase)
    
    if not length:
        print("You must specify password length!")
    
    if has_digits:
        chars.extend(string.digits)
    if has_uppercase:
        chars.extend(string.ascii_uppercase)
    if has_symbols:
        chars.extend(string.punctuation)
        
    if not chars:
        raise ValueError("At least one charachters type must be selected!")
    
    if length < 8:
        print("Password length must at least 8 characters long.")
    elif length > 25:
        print("Password length must at least less than 25 characters long.")
    
    password = ''.join(random.choice(chars) for a in range(length))
    return password

def check_strength(password: str) -> str:
    
    checks = [
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char.isupper() for char in password),
        any(char in string.punctuation for char in password)
    ]
    
    score = sum(checks)
    
    if score == 4:
        return print(f"Very Strong! Score: {score}")
    elif score == 3:
        return print(f"Strong! Score: {score}")
    elif score == 2:
        return print(f"Meduim! Score: {score}")
    elif score == 1:
        return print(f"Weak! Score: {score}")
    else:
        return print("A error occured! Please try again!")
    
while True:
    user_input = int(input("Choose action: 1. Generate password, 2. Validate password, 3. Exit: "))
    if user_input == 1:
        length = int(input("Enter length: "))
        etc = [a.lower() == "true" for a in input("Enter params: ").strip().split()]
        password = generate_password(length, *etc)
        print(password)
        print("\033[31mYour password has been copied to your clipboard!\033[0m")
        pyperclip.copy(password)
    elif user_input == 2:
        check_strength(input("Enter the password you want to validate: "))
    elif user_input == 3:
        break