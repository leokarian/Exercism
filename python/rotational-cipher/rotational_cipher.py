def rot(char,key):
    nchar = ord(char) + key
    if char.isupper():
        if nchar > 90: nchar -= 26
    else:
        if nchar > 122: nchar -= 26
    return chr(nchar)
        

def rotate(text, key):
    tlist = list(text)
    for i, char in enumerate(tlist):
        tlist[i] = rot(char,key) if char.isalpha() else char
    return ''.join(tlist)    
