def sum_of_multiples(limit, multiples):
    return sum(set([i for num in multiples if num > 0 for i in range(num, limit, num)]))
