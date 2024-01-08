ACTIONS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str) -> list:
    hello = int(binary_str, 2)
    handshake = []
    for i, x in enumerate(ACTIONS):
        if hello & 1 << i:
            handshake.append(x)
    if hello & 1 << 4:
        handshake.reverse()
    return handshake


