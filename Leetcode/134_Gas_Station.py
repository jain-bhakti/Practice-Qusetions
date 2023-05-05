def canCompleteCircuit(gas, cost):
    current = 0
    total_cost = sum(cost)
    total_fuel = sum(gas)
    start = 0

    if total_fuel < total_cost:
        return -1

    for i in range(len(gas)):
        current += gas[i]-cost[i]
        if current < 0:
            start = i+1
            current = 0
    return start
        

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas,cost))




