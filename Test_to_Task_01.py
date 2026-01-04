import timeit     

from coins import find_coins_greedy, find_min_coins      # якщо файл coins.py

def bench(amount: int, number: int = 200, repeat: int = 5):
    t_g = min(timeit.repeat(lambda: find_coins_greedy(amount), number=number, repeat=repeat)) / number
    t_d = min(timeit.repeat(lambda: find_min_coins(amount), number=number, repeat=repeat)) / number
    return t_g, t_d

for amt in [113, 1000, 10_000, 50_000]:
    tg, td = bench(amt)
    print(f"amount={amt:>6}  greedy={tg:.9f}s  dp={td:.9f}s  dp/greedy≈{td/tg:.0f}x")
