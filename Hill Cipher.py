import numpy as np

# Function to generate key matrix
def generate_key_matrix(key_str, n):
    key_matrix = np.zeros((n, n))
    char_index = 0
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key_str[char_index]) % 65
            char_index += 1
    return key_matrix

# Function to encrypt plaintext using Hill Cipher
def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    ciphertext = ""
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)
    plaintext_matrix = np.zeros((n, int(len(plaintext) / n)))
    char_index = 0
    for i in range(n):
        for j in range(int(len(plaintext) / n)):
            plaintext_matrix[i][j] = ord(plaintext[char_index]) % 65
            char_index += 1
    for i in range(int(len(plaintext) / n)):
        ciphertext_matrix = np.dot(key_matrix, plaintext_matrix[:, i]) % 26
        for j in range(n):
            ciphertext += chr(int(ciphertext_matrix[j]) + 65)
    return ciphertext

# Function to decrypt ciphertext using Hill Cipher
def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = ""
    ciphertext = ciphertext.upper().replace(" ", "")
    ciphertext_matrix = np.zeros((n, int(len(ciphertext) / n)))
    char_index = 0
    for i in range(n):
        for j in range(int(len(ciphertext) / n)):
            ciphertext_matrix[i][j] = ord(ciphertext[char_index]) % 65
            char_index += 1
    inverse_key_matrix = np.linalg.inv(key_matrix)
    inverse_key_matrix = inverse_key_matrix.round().astype(int) % 26
    for i in range(int(len(ciphertext) / n)):
        plaintext_matrix = np.dot(inverse_key_matrix, ciphertext_matrix[:, i]) % 26
        for j in range(n):
            plaintext += chr(int(plaintext_matrix[j]) + 65)
    return plaintext

# Example usage
key_str = "HILL"
key_matrix = generate_key_matrix(key_str, 2)
plaintext = input("Enter your secret message: ")
ciphertext = encrypt(plaintext, key_matrix)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, key_matrix)
print("Decrypted plaintext:", decrypted_plaintext)
