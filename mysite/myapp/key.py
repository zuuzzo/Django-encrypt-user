import os
import binascii

# Generate a random key
key = os.urandom(16)

# Convert the key to a string of hexadecimal digits
hex_key = binascii.hexlify(key).decode()

# Save the key to a file named key.txt
with open('mysite\myapp\key.txt', 'w') as f:
    f.write(hex_key)

print('Key saved to key.txt')