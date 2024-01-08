def square_root(number):
    # Easier in one line => return number ** 0.5   :-P
    i = 0
    while i**2 < number:
        i += 1
    return i
