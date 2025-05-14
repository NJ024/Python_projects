import random

chars = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()?QWERTYUIOPASDFGHJKLZXCVBNM"
length = int(input("Enter the length of the password: "))
password = ""  # Removed space before initialization

for _ in range(length):
    password += random.choice(chars)

print("Generated Password:", password)  # Prints the final password once
