class VigenereCipher:
    def __init__(self, key):
        self.key = key.lower()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encode(self, plaintext):
        plaintext = plaintext.lower()
        ciphertext = ''
        key_index = 0
        for char in plaintext:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.alphabet.index(self.key[key_index])) % 26
                ciphertext += self.alphabet[index]
                key_index = (key_index + 1) % len(self.key)
            else:
                ciphertext += char
        return ciphertext

    def decode(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.alphabet.index(self.key[key_index])) % 26
                plaintext += self.alphabet[index]
                key_index = (key_index + 1) % len(self.key)
            else:
                plaintext += char
        return plaintext


cipher = VigenereCipher(key='secret')

plaintext = input("Enter your secret message: ")
ciphertext = cipher.encode(plaintext)
print("Encoded message:", ciphertext)

decrypted_text = cipher.decode(ciphertext)
print("Decoded message:", decrypted_text)
