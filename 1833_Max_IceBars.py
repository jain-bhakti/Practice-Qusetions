def maxIceCream(costs, coins):
    count = 0
    costs.sort()
    for i in costs:
        if i <= coins:
            count += 1
            coins = coins-i

    return count

costs = [1,3,2,4,1]
coins = 7
print(maxIceCream(costs,coins))

