import random
import string

def generate_password(length=12):
    """Generate a random password with specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    """Generate multiple random passwords."""
   passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))
        if num_passwords <= 0 or password_length <= 0:
            raise ValueError("Number of passwords and length must be positive integers.")
        
        generated_passwords = generate_multiple_passwords(num_passwords, password_length)
        
        print("\nGenerated Passwords:")
        for password in generated_passwords:
            print(password)
    except ValueError as ve:
        print("Error:", ve)

