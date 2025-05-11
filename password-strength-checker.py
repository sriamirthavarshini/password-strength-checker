import re

def check_strength(password):
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2 or score == 3:
        return "Medium"
    else:
        return "Strong"

# Get user input
user_password = input("Enter your password: ")
strength = check_strength(user_password)
print(f"Your password strength is: {strength}")