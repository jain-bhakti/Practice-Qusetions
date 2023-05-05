#Brute Force
# O(n^2)
def buy_and_sell_stock_once(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if (prices[j] - prices[i]) > profit:
                profit = prices[j] - prices[i]
               
    return profit

    
#Efficient
#O(n)
def efficient(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit


prices = [310,315,275,295,260,270,290,230,255,250]
print(buy_and_sell_stock_once(prices))
print(efficient(prices))
