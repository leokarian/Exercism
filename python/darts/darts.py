def score(x, y):
    res = pow(x,2) + pow(y,2)
    if res > 100: return 0
    if 25 < res <= 100: return 1
    if 1 < res <= 25: return 5
    if 0 <= res <= 1: return 10
