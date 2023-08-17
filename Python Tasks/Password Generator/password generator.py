#Task 3: Password Generator

import random
import string

password_length = int(input("Enter the desired password length: "))

#Sequence os the password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))
print("Generated password:", password)