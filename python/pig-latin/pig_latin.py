import string


def translate(text):
    vowels = {"a", "e", "i", "o", "u"}
    consonants = set(string.ascii_lowercase).difference(vowels)
    words = []
    for word in text.split():
        if word[0] in vowels or "xr" == word[0:2] or "yt" == word[0:2]:
            words.append(word + "ay")
        elif word[0] in consonants:
            if "y" in word[1:-1]:
                if "y" == word[0]:
                    words.append(word[1:] + "yay")
                else:
                    words.append(word[word.index("y"):] + word[:word.index("y")] + "ay")
            elif "qu" == word[:2]:
                words.append(word[2:] + word[:2] + "ay")
            elif "qu" == word[1:3]:
                words.append(word[3:] + word[:3] + "ay")
            else:
                i = 1
                while word[i] in consonants and word[i] != 'y':
                    i += 1
                words.append(word[i:] + word[0:i] + "ay")
    return ' '.join(words)
