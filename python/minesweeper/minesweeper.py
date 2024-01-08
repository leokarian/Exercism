def is_a_mine_here(minefield: list, x: int, y: int) -> bool:
    return (len(minefield) > x >= 0 and
            len(minefield[x]) > y >= 0 and
            minefield[x][y] == "*")


def mines_around(minefield: list, x: int, y: int) -> int:
    return sum([is_a_mine_here(minefield, x - 1, y - 1),
                is_a_mine_here(minefield, x - 1, y),
                is_a_mine_here(minefield, x - 1, y + 1),
                is_a_mine_here(minefield, x, y - 1),
                is_a_mine_here(minefield, x, y + 1),
                is_a_mine_here(minefield, x + 1, y - 1),
                is_a_mine_here(minefield, x + 1, y),
                is_a_mine_here(minefield, x + 1, y + 1),
                ])


def annotate(minefield):
    # Function body starts here
    rows = len(minefield)
    if not rows: return []
    cols = len(minefield[0])
    if not cols: return minefield
    for i, row in enumerate(minefield):
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")
        row = list(row)
        for j, char in enumerate(row):
            if char not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")
            if char == " ":
                row[j] = str(mines_around(minefield, i, j) or " ")
        minefield[i] = ''.join(row)
    return minefield


