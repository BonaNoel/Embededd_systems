def caesar(msg, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    for c in msg:
        if alphabet.find(c) == -1:
            position = alphabet.find(c.lower())
            new_position = (position + key) % len(alphabet)
            new_character = alphabet[new_position]
            new_message += new_character.upper()
        else:
            position = alphabet.find(c)
            new_position = (position + key) % len(alphabet)
            new_character = alphabet[new_position]
            new_message += new_character
    return new_message


key = 3
while True:
    message = input("Please enter a message: ")
    if message == "q":
        break
    encry_message = caesar(message, key)
    decry_message = caesar(encry_message, -key)
    print("Encrypted message: ", encry_message)
    print("Decrypted message: ", decry_message)
