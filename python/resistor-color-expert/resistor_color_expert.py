COLORS = ["black", "brown", "red", "orange",
          "yellow", "green", "blue", "violet", "grey", "white"]
MAGNITUDE = ["ohms", "kiloohms", "megaohms", "gigaohms"]
TOLERANCE = {"grey": "0.05", "violet": "0.1", "blue": "0.25", "green": "0.5",
             "brown": "1", "red": "2", "gold": "5", "silver": "10"}


def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    if len(colors) == 4:
        col1, col2, mul, tol = colors
        res_val = COLORS.index(col1) * 10 + COLORS.index(col2)
        mag_val = 10 ** COLORS.index(mul)
    if len(colors) == 5:
        col1, col2, col3, mul, tol = colors
        res_val = COLORS.index(col1) * 100 + COLORS.index(col2) * 10 + COLORS.index(col3)
        mag_val = 10 ** COLORS.index(mul)

    ohms = float(res_val * mag_val)
    mag = 0
    while ohms > 1000:
        ohms /= 1000
        mag += 1
    return f"{ohms:g} {MAGNITUDE[mag]} ±{TOLERANCE[tol]}%"
