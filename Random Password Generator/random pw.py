import secrets
import string

# Function to generate password
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    if not any([include_uppercase, include_lowercase, include_numbers, include_symbols]):
        print("Error: Please select at least one character set.")
        return None
    
    character_pool = ""
    
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation
    
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

# Function to copy password to clipboard (optional, requires external libraries)
def copy_to_clipboard(password):
    try:
        import pyperclip
        pyperclip.copy(password)
        print("Password copied to clipboard!")
    except ImportError:
        print("pyperclip module not installed. Install it with 'pip install pyperclip'.")

def main():
    try:
        length = int(input("Enter password length (8-32): "))
        if length < 8 or length > 32:
            print("Error: Password length must be between 8 and 32.")
            return
        
        include_uppercase = input("Include Uppercase Letters? (y/n): ").strip().lower() == 'y'
        include_lowercase = input("Include Lowercase Letters? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include Numbers? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include Symbols? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
        
        if password:
            print(f"Generated Password: {password}")
            copy = input("Copy to clipboard? (y/n): ").strip().lower()
            if copy == 'y':
                copy_to_clipboard(password)
    
    except ValueError:
        print("Invalid input. Please enter a number for the password length.")

if __name__ == "__main__":
    main()


