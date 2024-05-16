import random
import string

def generate_password(length):
    if length < 6:
        return "Password should be at least 6 characters long."

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Get password length from user
length = int(input("Enter the desired password length (minimum 6 characters): "))
password = generate_password(length)

print(f"Generated Password: {password}")
