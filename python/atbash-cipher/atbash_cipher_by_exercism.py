from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(text: str):
    res = "".join(char for char in text.lower() if char.isalnum()).translate(ENCODING)
    return " ".join(res[index:index+5] for index in range(0, len(res), 5))


def decode(text: str):
    return "".join(char.lower() for char in text if char.isalnum()).translate(ENCODING)