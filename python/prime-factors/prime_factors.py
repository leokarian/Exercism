def factors(value: int) -> list[int]:
    l_factors = []
    prod = 2
    while value > 1:
        if value % prod == 0:
            l_factors.append(prod)
            value /= prod
        else:
            prod += 1
    return l_factors
