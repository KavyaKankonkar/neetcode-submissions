class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       #representing stock with line graph on day v/s stock price in $
       #we can understand from graph that the stock should not be purchased when ahead price goes down ,we should buy stock when next price is greater than current price of stock
       profit=0
       for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            profit+=prices[i+1]-prices[i]

       return profit