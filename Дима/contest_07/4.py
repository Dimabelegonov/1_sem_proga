def make_exchange(money, coins):
    coins.sort()
    return exchange_count(money, len(coins), coins)


def exchange_count(money, kinds_of_coins, coins):
    if money == 0:
        return 1
    if money < 0 or kinds_of_coins == 0:
        return 0
    else:
        return exchange_count(money, kinds_of_coins - 1, coins) \
               + exchange_count(money - coins[kinds_of_coins - 1],
                                kinds_of_coins, coins)
