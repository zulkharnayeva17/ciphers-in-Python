def shift_cipher(message, key, mode):

    result = ""
    if mode == "encrypt":
        shift = key
    elif mode == "decrypt":
        shift = -key
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    for char in message:
        if char.isalpha():

            new_code = ord(char) + shift

            if char.islower() and new_code > ord('z'):
                new_code -= 26
            elif char.isupper() and new_code > ord('Z'):
                new_code -= 26
            elif char.islower() and new_code < ord('a'):
                new_code += 26
            elif char.isupper() and new_code < ord('A'):
                new_code += 26

            new_char = chr(new_code)
            result += new_char
        else:
            result += char

    return result
message = input("Enter your secret message: ")
key = 3
encoded_message = shift_cipher(message, key, "encrypt")
print("Encoded message: " + encoded_message)
decoded_message = shift_cipher(encoded_message, key, "decrypt")
print("Decoded message: " + decoded_message)
