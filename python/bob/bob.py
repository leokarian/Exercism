def is_question(hb):
    return hb.endswith("?")


def is_yelling(hb):
    return hb.isupper()


def is_silence(hb):
    return len(hb) == 0


def response(hey_bob):
    hey_bob = hey_bob.strip()
    if is_silence(hey_bob):
        return "Fine. Be that way!"
    elif is_yelling(hey_bob) and is_question(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif is_yelling(hey_bob):
        return "Whoa, chill out!"
    elif is_question(hey_bob):
        return "Sure."
    else:
        return "Whatever."
