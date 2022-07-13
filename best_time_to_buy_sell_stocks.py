## We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. 
## Also, the second number (selling price) must be larger than the first one (buying price).
## In formal terms, we need to find max(prices[j]−prices[i]) for every j>i
## 


  def maxProfit(self, prices: List[int]) -> int:
      max_profit = 0
      for i in range(len(prices)-1):
          for j in range(i+1, len(prices)):
              profit = prices[j] - prices[i]
              if profit > max_profit:
                  max_profit = profit
      return max_profit
    
    
    ## compare profit with max profit or rather check for greater profit
