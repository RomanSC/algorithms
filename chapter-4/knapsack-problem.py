""" knapsack-problem.py
"""
def knapsack(coins, total):
    get_total = total
    n_coins = 0

    for coin in coins:
        print('COIN: {}'.format(coin))

        while get_total != 0:
            get_total -= coin
            n_coins += 1

    return n_coins

def main():
    coins = [1, 5, 10, 25]
    total = 63

    print(knapsack(coins, total))

if __name__=='__main__':
    main()
