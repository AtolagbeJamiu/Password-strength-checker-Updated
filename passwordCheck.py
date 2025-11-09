# Display the rules for password strength
print("===========================================")
print("      PASSWORD STRENGTH EVALUATION SYSTEM  ")
print("===========================================\n")

print("Rules for a STRONG password:")
print("- Must be at least 12 characters long.")
print("- Must contain at least one uppercase letter.")
print("- Must contain at least one lowercase letter.")
print("- Must contain at least one number.")
print("- Must contain at least one special character (e.g. @, #, $, %, &, *).")
print("\nA WEAK password usually:")
print("- Is too short (less than 12 characters).")
print("- Contains only letters or only numbers.")
print("- Does not include uppercase or special symbols.\n")

# Ask the user for a password
password = input("Enter your password to check its strength: ")

# Define the rules
min_length = 12
has_lower = any(ch.islower() for ch in password)
has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in "!@#$%^&*()_+=-" for ch in password)

# Track issues
problems = []

# Check each rule
if len(password) < min_length:
    problems.append(f"- Password should be at least {min_length} characters long.")
if not has_lower:
    problems.append("- Password should contain at least one lowercase letter.")
if not has_upper:
    problems.append("- Password should contain at least one uppercase letter.")
if not has_digit:
    problems.append("- Password should contain at least one number.")
if not has_special:
    problems.append("- Password should contain at least one special character (e.g. @, #, $, %).")

# Give feedback
print("\nRESULT:")
if not problems:
    print("Your password is STRONG. It meets all the security requirements.")
else:
    print("Your password is WEAK because:")
    for issue in problems:
        print(issue)

