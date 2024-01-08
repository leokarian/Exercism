def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    for val, name in [(input_base, "input"), (output_base, "output")]:
        if val < 2:
            raise ValueError(f"{name} base must be >= 2")

    decimal = 0
    for i, d in enumerate(reversed(digits)):
        if not 0 <= d < input_base: raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal += d * (input_base ** i)

    n_digits = []
    while decimal:
        n_digits.append(decimal % output_base)
        decimal = decimal // output_base
    n_digits.reverse()
    return n_digits or [0]
