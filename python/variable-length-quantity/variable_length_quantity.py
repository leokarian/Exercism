def encode(numbers):
    results = []
    for num in numbers:
        num_vals = []
        while num != 0:
            num_vals.insert(0, num & 0x7F)
            num = num >> 7
        for i, n in enumerate(num_vals[:-1]):
            num_vals[i] = n | 0x80
        if len(num_vals) == 0:
            num_vals.append(0)
        results += num_vals
    return results

def decode(bytes_):
    if len(bytes_) > 0 and bytes_[-1] & 0x80 > 0:
        raise ValueError('incomplete sequence')
    result = []
    x = 0
    for num in bytes_:
        x = (x << 7) | (num & 0x7f)
        if num & 0x80 == 0:
            result.append(x)
            x = 0
    return result
