BRACKETS = {"(": ")", "[": "]", "{": "}"}
END_BRACKETS = (")", "]", "}")


def is_paired(input_string: str) -> bool:
    stack = []
    for char in input_string:
        if char in BRACKETS:
            stack.append(BRACKETS[char])
        elif char in END_BRACKETS and not (stack and stack.pop() == char):
            return False
    return not stack
