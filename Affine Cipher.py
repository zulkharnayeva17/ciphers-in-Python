class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.mod_inverse = self.get_modular_inverse(self.a, len(self.alphabet))

    def encode(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.lower() in self.alphabet:
                index = self.alphabet.index(char.lower())
                if char.isupper():
                    ciphertext += self.alphabet[(self.a * index + self.b) % 26].upper()
                else:
                    ciphertext += self.alphabet[(self.a * index + self.b) % 26]
            else:
                ciphertext += char
        return ciphertext

    def decode(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.lower() in self.alphabet:
                index = self.alphabet.index(char.lower())
                if char.isupper():
                    plaintext += self.alphabet[(self.mod_inverse * (index - self.b)) % 26].upper()
                else:
                    plaintext += self.alphabet[(self.mod_inverse * (index - self.b)) % 26]
            else:
                plaintext += char
        return plaintext

    def get_modular_inverse(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

cipher = AffineCipher(a=5, b=8)

plaintext = input("Enter your secret message: ")
ciphertext = cipher.encode(plaintext)
print("Encoded message:", ciphertext)

decrypted_text = cipher.decode(ciphertext)
print("Decoded message:", decrypted_text)
