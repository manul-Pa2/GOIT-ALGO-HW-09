from __future__ import annotations

from typing import Dict, List


COINS: List[int] = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int, coins: List[int] = COINS) -> Dict[int, int]:
    """
    Жадібний алгоритм:
    - завжди беремо найбільшу монету, яку можемо.
    Повертає {номінал: кількість}
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")

    coins = sorted(coins, reverse=True)
    result: Dict[int, int] = {}

    for coin in coins:
        if amount == 0:
            break
        cnt, amount = divmod(amount, coin)
        if cnt:
            result[coin] = cnt

    return result


def find_min_coins(amount: int, coins: List[int] = COINS) -> Dict[int, int]:
    """
    Динамічне програмування:
    - знаходить розклад суми з мінімальною кількістю монет.
    Повертає {номінал: кількість}
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if amount == 0:
        return {}

    coins = sorted(coins)  
    INF = 10**18

    # мін. кількість монет для суми
    dp = [0] + [INF] * amount
    # яка монета була взята останньою
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for s in range(coin, amount + 1):
            if dp[s - coin] + 1 < dp[s]:
                dp[s] = dp[s - coin] + 1
                coin_used[s] = coin

    if dp[amount] == INF:  
        return {}

    # оновлення відповіді
    result: Dict[int, int] = {}
    s = amount
    while s > 0:
        coin = coin_used[s]
        if coin == 0:        # захист від некоректної реконструкції
            return {}
        result[coin] = result.get(coin, 0) + 1
        s -= coin

    return result


if __name__ == "__main__":
    amount = 113
    print("Greedy:", find_coins_greedy(amount))
    print("DP    :", find_min_coins(amount))
