import string

def is_pangram(sentence):
    return len(set(string.ascii_lowercase).intersection(set(sentence.lower()))) == 26
