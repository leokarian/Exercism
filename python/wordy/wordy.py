def answer(question: str):
    operators = ("+", "-", "*", "/")
    question = question.strip().replace("by ", "")
    if not question.startswith("What is") or not question.endswith("?") or "cubed" in question:
        raise ValueError("unknown operation")
    question = question.removeprefix("What is")\
        .removesuffix("?")\
        .replace("plus", "+")\
        .replace("minus", "-")\
        .replace("multiplied", "*")\
        .replace("divided", "/")\
        .split()
    q_numbers = question[0::2]
    q_operations = question[1::2]

    try:
        # Checks for numbers and operators in correct order
        for n in q_numbers:
            int(n)
        for op in q_operations:
            if op not in operators:
                raise ValueError("syntax error")

        # return the value if it's only a number
        if len(q_numbers) == 1 and len(q_operations) == 0:
            return eval(q_numbers[0])

        n_q = ["(", q_numbers[0], q_operations[0], q_numbers[1], ")"]
        q_numbers = q_numbers[2:]
        for i, op in enumerate(q_operations[1:]):
            n_q.insert(0, "(")
            n_q.append(op)
            n_q.append(q_numbers[i])
            n_q.append(")")

        new_question = ' '.join(n_q)
        return eval(new_question)
    except Exception as err:
        raise ValueError("syntax error")


print(answer("What is -3 plus 7 multiplied by -2?"))
