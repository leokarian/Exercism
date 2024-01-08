def find(search_list: list, value: int) -> int:
    low, high = 0, len(search_list)
    while low < high:
        mid = (high + low) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            high = mid
        else:
            low = mid + 1
    raise ValueError("value not in array")