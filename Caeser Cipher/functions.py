def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_char = chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                encrypted_char = chr((ord(char) - start + shift_amount) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)