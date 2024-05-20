import random
import string

def generate_password(length):
    # Define the character set including letters (both lowercase and uppercase) and digits
    characters = string.ascii_letters + string.digits
    # Generate a random password by randomly choosing characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    # Example usage: generate a random password with length 10
    password = generate_password(10)
    print("Random password:", password)
    choice = input("Do you want to generate another password? (yes/no): ")
    if choice.lower() != 'yes':
        break
