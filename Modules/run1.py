import string

def validate_password(password, min_length=8):
    """Check if password meets all criteria."""
    if len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        return False
    if not any(c.isupper() for c in password):
        print("Password must contain at least 1 uppercase letter.")
        return False
    if not any(c.islower() for c in password):
        print("Password must contain at least 1 lowercase letter.")
        return False
    if not any(c.isdigit() for c in password):
        print("Password must contain at least 1 number.")
        return False
    if not any(c in string.punctuation for c in password):
        print("Password must contain at least 1 symbol (e.g., !@#$%).")
        return False
    return True

# Main program
print("Create your password (must include uppercase, lowercase, number, symbol):")

while True:
    user_password = input("Enter password: ")
    if validate_password(user_password):
        print("✅ Your password is valid and strong!")
        break
    else:
        print("❌ Please try again.\n")