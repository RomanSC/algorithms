def greedy(coins=[0.01, 0.05, 0.10, 0.25], needed_value=0.63):
    n_coins = 0 # Holds least # of coins for needed_value
    running_total = needed_value

    while running_total != 0:
        for n in coins:
            if coins < needed_value:
                #TODO:
                # stuff

def main():
    pass

if __name__ == '__main__':
    main()
