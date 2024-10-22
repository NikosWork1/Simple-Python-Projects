import re 

def validate_password(password):
    if (len(password) >= 8 and                       # At least 8 characters long
        re.search(r"[a-z]", password) and            # Contains at least one lowercase letter
        re.search(r"[A-Z]", password) and            # Contains at least one uppercase letter
        re.search(r"[0-9]", password) and            # Contains at least one digit
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):  # Contains at least one special character
        return True  # Password is valid
    else:
        return False  # Password is invalid

password_input = input("Enter a password to validate: ")

if validate_password(password_input):
    print("Password is valid.")
else:
    print("Password is invalid. Please ensure it meets the criteria:")
    print("- At least 8 characters long")
    print("- Contains both uppercase and lowercase letters")
    print("- Contains at least one numerical digit")
    print("- Contains at least one special character (e.g., !, @, #, ?, etc.)")
