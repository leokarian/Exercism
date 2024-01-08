# Formulas obtained from:
# https://learnersbucket.com/examples/algorithms/difference-between-square-of-sum-of-numbers-and-sum-of-square-of-numbers/
def square_of_sum(number):
    # return sum([num for num in range(1, number+1)]) ** 2
    return ((number * (number + 1)) / 2) ** 2


def sum_of_squares(number):
    # return sum([(num ** 2) for num in range(1, number+1)])
    return (number * (number + 1) * ((number * 2) + 1)) / 6


def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))
