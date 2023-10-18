def caesar_decipher(secret, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = ""
    for char in secret:
        position = alphabet.find(str(char))
        new_position = (position - key) % len(alphabet)
        message += alphabet[new_position]
    return message


encrypted_message = "iqfihhih"

for key in range(1, 26):
    print("Message: ", caesar_decipher(
        encrypted_message, key), "| Key: ", key)
