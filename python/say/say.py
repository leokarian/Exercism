ONES = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'ninteen',
]
TENS = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety']
BASES = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (1e2, 'hundred'),
)


def say(number: int) -> str:
    sections = []
    if not 0 <= number < 1e12:
        raise ValueError("input out of range")

    if number == 0:
        return ONES[number]

    for base, name in BASES:
        if number >= base:
            sections.append(say(int(number // base)))
            sections.append(name)
            number = int(number % base)

    units = ""
    if number >= 20:
        units += TENS[number // 10]
        number = int(number % 10)
        if number:
            units += "-"
    if number and number < 20:
        units += ONES[number]
    if units:
        sections.append(units)

    return ' '.join(sections)
