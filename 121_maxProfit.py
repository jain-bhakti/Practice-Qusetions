prices = [7,1,5,3,6,4]
n = len(prices)
l = 0
r = 1
maxProfit = 0
while(r<len(prices)):
    if prices[r] > prices[l]:
        profit = prices[r] - prices[l]
        maxProfit = max(maxProfit , profit)                
    else:
        l = r
    r += 1

        

print(maxProfit)

