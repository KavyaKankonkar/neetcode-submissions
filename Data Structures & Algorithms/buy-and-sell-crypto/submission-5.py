class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit,profit=prices[0],0 
        for i,p in enumerate(prices):
            profit=max(profit,p-min_profit)
            min_profit=min(min_profit,p)

        return profit

