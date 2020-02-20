# coins.py
# Alex Harris
# 11/25/19

# ----------------------------------------------------------------------

def main():
    coins = input("Please enter your coin values, without the 1, separated by a space in order (ex. 5 11): ")
    coins = coins.split()
    coins.insert(0, '1')
    for i in range(len(coins)):
        coins[i] = int(coins[i])
    coinsFinal = {}
    for i in range(1, 100):
        # if it's the first coin, you need 1 coin being 1
        if i == 1:
            coinsFinal[i] = [1, [1]]
        else:
            j = 1
            # assume the previous is the smallest number of coins for current
            coinsFinal[i] = [coinsFinal[i-1][0], coinsFinal[i-1][1][:]]
            # while current amount is greater than the coin value

            while i >= coins[j]:
                # if the amount is one the current coin
                if i == coins[j]:
                    # the final is one coin
                    coinsFinal[i] = [1, []]
                    j += 1
                    if j == len(coins):
                        break

                else:
                    # else check that other coin options don't have less coins
                    check = [coinsFinal[i - coins[j]][0], coinsFinal[i - coins[j]][1][:]]
                    # if we find an amount of coins less than what we have it
                    if coinsFinal[i][0] > check[0]:
                        # set the coins of current amount to that amount
                        coinsFinal[i] = check[:]
                    j += 1
                    if j == len(coins):
                        break

            # initialize the variable to see what coin we need
            whileCheck = i
            # subtract the other coins values
            for j in coinsFinal[i][1]:
                whileCheck -= j
            # append what is left over AKA the coin we need
            coinsFinal[i][1].append(whileCheck)
            # set the amount of coins to how many coins are needed
            coinsFinal[i][0] = len(coinsFinal[i][1])

        # print what coin we're on
        print("amount:", i, end="")
        # print the number of coins
        print(", number of coins:", coinsFinal[i][0], end="")
        # print which coins we used, sorted
        print(", coins:", end=" ")
        coinsFinal[i][1].sort()
        print(coinsFinal[i][1], end=", ")
        # double check that the sum of the coins we used is the amount we were trying to get
        total = 0
        for j in range(len(coinsFinal[i][1])):
            total += coinsFinal[i][1][j]
        print("total:", total)

# ----------------------------------------------------------------------

if __name__ == "__main__":
    main()