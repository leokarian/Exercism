from string import ascii_uppercase
LETTERS = ascii_uppercase


def get_line(char, spaces):
    if char == "A":
        line = spaces * " " + char + spaces * " "
        print(line)
    else:
        side_sp = " " * (spaces - LETTERS.index(char))
        mid_sp = (LETTERS.index(char) * 2 - 1) * " "
        line = side_sp + char + mid_sp + char + side_sp
    return line


def rows(letter):
    diamond = []
    spaces = LETTERS.index(letter)
    index = spaces
    for char in LETTERS[:index + 1]:
        diamond.append(get_line(char, spaces))

    # The bottom part is the mirror of the top part without the center line
    return diamond + diamond[-2::-1]
