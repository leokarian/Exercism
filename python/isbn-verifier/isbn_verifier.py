def is_valid(isbn: str) -> bool:
    isbn = isbn.replace("-","")
    if len(isbn) != 10: return False
    nums = list(isbn)
    if nums[-1] == 'X':
        nums[-1] = '10'
    if not all(num.isdigit() for num in nums):
        return False
    count = sum(int(nums[index]) * x for index, x in enumerate(list(range(10, 0, -1))))
    return count % 11 == 0
