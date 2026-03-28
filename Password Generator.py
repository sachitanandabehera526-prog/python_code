import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits 

    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter your password length:"))
password = generate_password(length)
print("Your password is:",password)