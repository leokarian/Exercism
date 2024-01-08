NUMBERS = [[" _ ", "| |", "|_|", "   "], ["   ", "  |", "  |", "   "], [" _ ", " _|", "|_ ", "   "],
           [" _ ", " _|", " _|", "   "], ["   ", "|_|", "  |", "   "], [" _ ", "|_ ", " _|", "   "],
           [" _ ", "|_ ", "|_|", "   "], [" _ ", "  |", "  |", "   "], [" _ ", "|_|", "|_|", "   "],
           [" _ ", "|_|", " _|", "   "]]


def chunks(lst):
    lines = []
    for i in range(0, len(lst), 4):
        lines.append(lst[i:i + 4])
    return lines


def get_number(line):
    for i in range(0, len(line[0]), 3):
        yield [line[0][i:i + 3], line[1][i:i + 3], line[2][i:i + 3], line[3][i:i + 3]]


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for col in input_grid:
        if len(col) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    num = ''
    lines = chunks(input_grid)
    for line in lines:
        for n in get_number(line):
            if n in NUMBERS:
                num += str(NUMBERS.index(n))
            else:
                num += '?'
        num += ','
    return num[:-1]
