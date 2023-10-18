def caesar_encryption(msg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    private_key = 19
    encry_message = ""

    for c in msg:
        position = alphabet.find(c)
        new_position = (position + private_key) % len(alphabet)
        new_character = alphabet[new_position]
        encry_message += new_character

    return encry_message


def caesar_decryption(msg, public_key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    private_key = 23
    decry_message = ""
    key = int(public_key / private_key)

    for c in msg:
        position = alphabet.find(c)
        new_position = (position - key) % len(alphabet)
        new_character = alphabet[new_position]
        decry_message += new_character

    return decry_message


message = input("Please enter a message: ")
print("Encrypted message: ", caesar_encryption(message))
print("Decrypted message: ", caesar_decryption(
    caesar_encryption(message), 19*23))
