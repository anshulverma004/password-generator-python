import string
import secrets

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one character from each set
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols

    # Fill remaining length
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# User input
length = int(input("Enter password length: "))
strong_password = generate_password(length)

print("Generated Strong Password:", strong_password)
