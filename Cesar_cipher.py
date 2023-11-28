alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position + shift_amount
        if new_position > 25:
            new_position -= 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for i in cipher_text:
        position = alphabet.index(i)
        old_position = position - shift_amount
        if old_position < 0:
            old_position += 26
        new_letter = alphabet[old_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")


if direction.lower() == 'encode':
    encrypt(text, shift)
elif direction.lower() == 'decode':
    decrypt(text, shift)
else:
    print("Please type 'encode' or 'decode'")
