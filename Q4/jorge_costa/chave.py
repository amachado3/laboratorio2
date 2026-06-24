import json
import socket
from cryptography.fernet import Fernet

# Put this somewhere safe!
key = Fernet.generate_key()
print("Generated key: ", key)

file = input("Enter the filename to save the key (e.g., key.fernet): ")
with open(file, 'wb') as key_file:
    key_file.write(key)
    print(f"Key saved to {file}")
    