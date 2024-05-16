import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and has_upper and has_lower and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

# Get password from user
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)

print(f"Password Strength: {strength}")
