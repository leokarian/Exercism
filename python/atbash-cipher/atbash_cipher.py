PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"
MAP = dict(zip(PLAIN, CIPHER))


def code(text):
    return ''.join([MAP[char] if char in MAP else char for char in text if char.isalnum()])


def encode(plain_text: str):
    cipher_text = code(plain_text.lower())
    return ' '.join([cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5)])


def decode(ciphered_text):
    return code(ciphered_text)
