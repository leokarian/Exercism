COLORS = ["black", "brown", "red", "orange",
          "yellow", "green", "blue", "violet", "grey", "white"]
MAGNITUDE = ["ohms", "kiloohms", "megaohms", "gigaohms"]


def label(colors: list[str]) -> str:
    col1, col2, col3, *garbage = colors
    res_val = COLORS.index(col1) * 10 + COLORS.index(col2)
    mag_val = 10 ** COLORS.index(col3)
    ohms = res_val * mag_val

    mag = 0
    while ohms > 1000 and not ohms % 1000:
        ohms //= 1000
        mag += 1
    return " ".join([str(ohms), MAGNITUDE[mag]])
