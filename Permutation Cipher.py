import random

def encode(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = dict(zip(alphabet, key))

    encoded = ""
    for c in message.upper():
        if c in mapping:
            encoded += mapping[c]
        else:
            encoded += c

    return encoded


def decode(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = dict(zip(key, alphabet))

    decoded = ""
    for c in message.upper():
        if c in mapping:
            decoded += mapping[c]
        else:
            decoded += c

    return decoded

key = "XPMGTDHLYONZBWEARKJUFSCIQV"
message = input("Enter your secret message: ")

encoded_message = encode(message, key)
print("Encoded message:", encoded_message)

decoded_message = decode(encoded_message, key)
print("Decoded message:", decoded_message)
