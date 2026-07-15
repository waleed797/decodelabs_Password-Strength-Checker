
import string


def check_password_strength(password):
    """
    Checks a password against length and character-type rules and
    returns its strength as "Weak", "Medium", or "Strong".
    """
    length = len(password)

    has_upper = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Count how many of the 3 required character types are present
    criteria_met = sum([has_upper, has_number, has_symbol])

    # --- Condition checks for strength classification ---
    if length < 6:
        strength = "Weak"
    elif length >= 6 and criteria_met <= 1:
        strength = "Weak"
    elif length >= 6 and criteria_met == 2:
        strength = "Medium"
    elif length >= 8 and criteria_met == 3:
        strength = "Strong"
    else:
        strength = "Medium"

    return strength, has_upper, has_number, has_symbol


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength, has_upper, has_number, has_symbol = check_password_strength(password)

    print("\n--- Result ---")
    print(f"Length: {len(password)} characters")
    print(f"Contains uppercase letter: {'Yes' if has_upper else 'No'}")
    print(f"Contains number: {'Yes' if has_number else 'No'}")
    print(f"Contains symbol: {'Yes' if has_symbol else 'No'}")
    print(f"\nPassword Strength: {strength}")


if __name__ == "__main__":
    main()
