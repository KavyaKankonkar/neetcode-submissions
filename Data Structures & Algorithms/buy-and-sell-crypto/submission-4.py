class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res,buy=0,0
        for i,p in enumerate(prices):
            buy=p
            for j in range(i+1,len(prices)):
                cost=prices[j]-p
                res=max(res,cost)

        return res

