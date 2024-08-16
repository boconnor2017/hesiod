# Simple Encryption Algorithm

import sys
from cryptography.fernet import Fernet

"""
Encryption is the process by which an algorithm converts plain text into "cypher text" (i.e. the scrambled format) 
using an encryption key. Decryption is the reverse process by which the algorithm decodes the cypher text into plain 
text using the same encryption key. In symmetric-key encryption, the data is encoded and decoded with the same key.

To execute this file, first run 'pip install cryptography'.  
"""

# Step 1: Prompt User for Plain Text
plaintextinput = input("Enter Plain Text: ")

# Step 2: Create Encryption Key
encryptionkey = Fernet.generate_key()

# Step 3: Encrypt the Plain Text
fernet = Fernet(encryptionkey)
cyphertext = fernet.encrypt(plaintextinput.encode())

# Step 4: Ouput Cypher Text and Encryption Key
print("Cypher Text: ", cyphertext)
print("Encryption Key: ", encryptionkey)
