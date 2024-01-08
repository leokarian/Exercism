def check_we(row: list, pos: int) -> bool:
    for p, x in enumerate(row):
        if p != pos:
            if x > row[pos]:
                return False
    return True


def check_ns(matrix: list, row: int, col: int) -> bool:
    for i, r in enumerate(matrix):
        if i != col:
            if r[col] < matrix[row][col]:
                return False
    return True


def saddle_points(matrix: list) -> list:
    if len(matrix):
        n_elem = len(matrix[0])
    points = []
    for i, r in enumerate(matrix):
        if len(r) != n_elem:
            raise ValueError("irregular matrix")
        for j, c in enumerate(r):
            if check_we(r, j) and check_ns(matrix, i, j):
                points.append({"row": i+1, "column": j+1})
    return points
