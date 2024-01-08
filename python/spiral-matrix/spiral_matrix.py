def spiral_matrix(size: int) -> list[list[int]]:
    # Initialize with zeroes
    result = [[0 for _ in range(size)] for _ in range(size)]
    x, y = 0, 0
    direction_x = [1, 0, -1, 0]
    direction_y = [0, 1, 0, -1]
    direction_index = 0

    for i in range(1, (size ** 2) + 1):
        result[y][x] = i
        x += direction_x[direction_index]
        y += direction_y[direction_index]

        if x >= size or y >= size or result[y][x]:
            # Go back 1 step
            x -= direction_x[direction_index]
            y -= direction_y[direction_index]

            # Change Direction
            direction_index = (direction_index + 1) % 4

            # Move forward 1 step
            x += direction_x[direction_index]
            y += direction_y[direction_index]

    return result
