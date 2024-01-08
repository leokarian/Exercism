# Recursive flatten approach
def flatten(iterable: list) -> list:
    new_list = []
    for item in iterable:
        if not isinstance(item, (list, set, tuple)) and item is not None:
            new_list.append(item)
        elif isinstance(item, (list, set, tuple)):
            new_list.extend(flatten(item))
    return new_list
