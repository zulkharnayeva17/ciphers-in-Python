import string
class SubstitutionCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = string.ascii_lowercase

    def encode(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.lower() in self.alphabet:
                index = self.alphabet.index(char.lower())
                if char.isupper():
                    ciphertext += self.key[index].upper()
                else:
                    ciphertext += self.key[index]
            else:
                ciphertext += char
        return ciphertext

    def decode(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.lower() in self.key:
                index = self.key.index(char.lower())
                if char.isupper():
                    plaintext += self.alphabet[index].upper()
                else:
                    plaintext += self.alphabet[index]
            else:
                plaintext += char
        return plaintext

key = 'qwertyuiopasdfghjklzxcvbnm'
cipher = SubstitutionCipher(key)

plaintext = input("Enter your secret message: ")

ciphertext = cipher.encode(plaintext)

print("Encrypted Text:", ciphertext)
decrypted_text = cipher.decode(ciphertext)
print("Decrypted Text", decrypted_text)