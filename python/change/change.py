from itertools import combinations_with_replacement


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []

    coin_list = []
    for i in range(1 + target // min(coins)):
        for c in combinations_with_replacement(coins, i):
            if sum(list(c)) == target:
                coin_list = coin_list + list(c)
                break
        if len(coin_list):
            return coin_list

    raise ValueError("can't make target with given coins")
