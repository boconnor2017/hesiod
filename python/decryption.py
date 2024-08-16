# Simple Decryption Algorithm

import sys
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode 

"""
Encryption is the process by which an algorithm converts plain text into "cypher text" (i.e. the scrambled format) 
using an encryption key. Decryption is the reverse process by which the algorithm decodes the cypher text into plain 
text using the same encryption key. In symmetric-key encryption, the data is encoded and decoded with the same key.

To execute this file, first run 'pip install cryptography'.  
"""

# Step 1: Prompt User for Cypher Text
cyphertextinput = input("Enter Cypher Text: ")
encryptionkeyinput = input("Enter Encryption Key: ")

# Step 2: Convert Input Strings to Byte Format
ct1 = cyphertextinput.replace("b", "", 1)
ct2 = ct1.replace("\'", "")
bytes_cyphertext = ct2.encode()

ek1 = encryptionkeyinput.replace("b", "", 1)
ek2 = ek1.replace("\'", "")
bytes_encryptionkey = ek2.encode()

# Step 3: Decrypt the Cypher Text
f = Fernet(bytes_encryptionkey)
plaintext = f.decrypt(bytes_cyphertext).decode()

# Step 3: Ouput Cypher Text and Encryption Key
print("Plan Text: ", plaintext)