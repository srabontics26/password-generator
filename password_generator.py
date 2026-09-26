import secrets
import string


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))

    return password


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


def main():
    print("=" * 45)
    print("Password Generator & Strength Checker")
    print("=" * 45)

    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            try:
                length = int(input("Enter password length: "))

                if length < 8:
                    print("Password length should be at least 8 characters.")
                    continue

                password = generate_password(length)

                print("\nGenerated Password:")
                print(password)
                print("Strength:", check_password_strength(password))

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            password = input("Enter your password: ")

            if not password:
                print("Password cannot be empty.")
                continue

            strength = check_password_strength(password)

            print("Password Strength:", strength)

        elif choice == "3":
            print("Thank you for using the Password Generator.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
