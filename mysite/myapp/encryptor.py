from Crypto.Cipher import AES
import os

def encrypt(message):
    with open('mysite\myapp\key.txt', 'rb') as key_file:
        key = key_file.read()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_EAX, iv)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    with open('mysite\myapp\output.txt', 'wb') as output_file:
        [output_file.write(x) for x in (iv, tag, ciphertext)]

    return ciphertext

# text = input("Enter text to encrypt: ")
# key_filename = "key.txt"
# encrypted_text = encrypt(text.encode(), key_filename)
# print("Encrypted text:", encrypted_text.hex())


from Crypto.Cipher import AES
import os

def decrypt(ciphertext_filename, key_filename):
    ciphertext_filename = 'output.txt'
    key_filename = 'mysite\myapp\key.txt'
    with open(ciphertext_filename, 'rb') as f:
        iv = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    with open(key_filename, 'rb') as key_file:
        key = key_file.read()

    cipher = AES.new(key, AES.MODE_EAX, iv)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext

# ciphertext_filename = 'output.txt'
# decrypted_text = decrypt(ciphertext_filename, key_filename)