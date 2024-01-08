def find_anagrams(word: str, candidates: list[str]) -> list:
    return [x for x in candidates if sorted(x.lower()) == sorted(word.lower()) and x.lower() != word.lower()]
