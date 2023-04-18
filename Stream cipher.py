import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def encrypt(key, plaintext):
    ciphertext = ''
    keystream = [ord(c) for c in key]
    for i, c in enumerate(plaintext):
        ciphertext += chr(ord(c) ^ keystream[i % len(key)])
    return ciphertext

def decrypt(key, ciphertext):
    plaintext = ''
    keystream = [ord(c) for c in key]
    for i, c in enumerate(ciphertext):
        plaintext += chr(ord(c) ^ keystream[i % len(key)])
    return plaintext

key = generate_key(16)
plaintext = input("Enter your secret message: ")
ciphertext = encrypt(key, plaintext)
decrypted = decrypt(key, ciphertext)

print(f"Key: {key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
