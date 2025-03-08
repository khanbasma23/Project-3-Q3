import re
import random

# Common weak passwords list
COMMON_PASSWORDS = {"password", "123456", "12345678", "qwerty", "abc123", "password1", "123456789"}

# Special characters for password security
SPECIAL_CHARACTERS = "!@#$%^&*"

def check_password_strength(password):
    score = 0
    feedback = []

    # Blacklist check
    if password.lower() in COMMON_PASSWORDS:
        return "❌ Weak Password - This password is too common. Choose a unique one."

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special character check
    if re.search(rf"[{re.escape(SPECIAL_CHARACTERS)}]", password):
        score += 1
    else:
        feedback.append(f"❌ Include at least one special character ({SPECIAL_CHARACTERS}).")

    # Strength rating
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions:\n" + "\n".join(feedback)

def generate_strong_password(length=12):
    """Generates a random strong password with a mix of characters"""
    if length < 8:
        length = 8  # Ensure minimum security standard

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = SPECIAL_CHARACTERS

    all_chars = lower + upper + digits + special
    password = (
        random.choice(lower)
        + random.choice(upper)
        + random.choice(digits)
        + random.choice(special)
        + "".join(random.choices(all_chars, k=length - 4))
    )

    return "".join(random.sample(password, len(password)))  # Shuffle for randomness

# --- Main Execution ---
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    print(check_password_strength(user_password))

    # Suggest a strong password if needed
    if "Weak Password" in check_password_strength(user_password):
        print("\n💡 Suggested Strong Password:", generate_strong_password())
