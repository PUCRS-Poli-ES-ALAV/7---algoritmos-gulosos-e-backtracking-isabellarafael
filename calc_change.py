from typing import Dict, List, Tuple


def calc_change(available_coins: List[int], amount: float) -> Tuple[Dict[int, int], int]:
    amount = int(amount * 100)
    res: Dict[int, int] = {coin: 0 for coin in available_coins}
    aux: int = 0

    iterations = 0
    while aux < amount:
        try:
            coin = max(
                filter(lambda val: val + aux <= amount, available_coins)
            )
        except ValueError:
            print('No solution')
            return {}, iterations
        res[coin] += 1
        aux += coin
        iterations += 1

    return res, iterations


print(calc_change([100, 25, 10, 5, 1], 2.89))
print(calc_change([100], 2.89))
