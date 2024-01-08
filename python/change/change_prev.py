def check_manual_change(coins: list[int], target: int) -> list[int]:
    tot = 0
    coin_list = []
    for c in coins:
        while (tot + c) <= target:
            coin_list.append(c)
            tot += c
    coin_list.reverse()
    return coin_list


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")
    coin_list = []
    coins.reverse()
    for i in range(0, len(coins)):
        coin_aux = check_manual_change(coins[i:], target)
        if not coin_list or len(coin_list) > len(coin_aux):
            coin_list = coin_aux
    if sum(coin_list) != target:
        raise ValueError("can't make target with given coins")
    return coin_list
