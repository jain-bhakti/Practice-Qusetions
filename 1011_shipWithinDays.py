def shipWithinDays(weights,days):
    weights.sort()
    for i in range(days):
        weights.pop()
    print(sum(weights))



weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shipWithinDays(weights,days))