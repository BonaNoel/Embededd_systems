from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def generate_otp(characters):
    with open("otp.txt", "w") as f:
        for i in range(characters):
            f.write(str(randint(0, 26)) + "\n")


def load_otp():
    with open("otp.txt", "r") as f:
        contents = f.read().splitlines()
    return contents


def encrypt(message, key):
    ciphertext = ''
    for (position, character) in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) +
                         int(key[position])) % len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext


def decrypt(message, key):
    ciphertext = ''
    for (position, character) in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) -
                         int(key[position])) % len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext


message = input("What do you want to encrypt: ")
generate_otp(len(message))
encrypt_message = encrypt(message, load_otp())
decrypt_message = decrypt(encrypt_message, load_otp())
print("Encrypted message: ", encrypt_message)
print("Decrypted message: ", decrypt_message)
