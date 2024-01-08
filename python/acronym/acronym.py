import re


def abbreviate(words: str) -> str:
    words = re.sub(r'[-_]', ' ', words).split()
    return ''.join([word[0].upper() for word in words])

