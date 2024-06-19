import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation  
    all_chars = lowercase_letters + uppercase_letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("Let's generate a password")
    while True:
        try:
            length = int(input("Enter the length of the password you'd like to generate: "))
            if length <= 0:
                print("Length must be greater than zero. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

