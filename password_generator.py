import random
import string

def generate_password(length=12, include_upper=True, include_numbers=True, include_symbols=True):
    chars = string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Password Generator")
    length = int(input("Enter length (min 8): ") or 12)
    if length < 8:
        length = 8
    upper = input("Include uppercase? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'
    password = generate_password(length, upper, numbers, symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
