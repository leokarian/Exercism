NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ROMAN = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


def roman(number: int) -> str:
    res = ""
    while number > 0:
        for i, n in enumerate(NUMBERS):
            while n <= number:
                res += ROMAN[i]
                number -= n

    return res
