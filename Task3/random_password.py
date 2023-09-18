import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity choice. Please choose from 'easy', 'medium', or 'strong'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    
    while True:
        length = input("Enter the desired password length: ")
        try:
            length = int(length)
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the length.")

    complexity = input("Choose complexity ('easy', 'medium', or 'strong'): ").lower()

    password = generate_password(length, complexity)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

