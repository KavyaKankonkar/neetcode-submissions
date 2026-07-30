class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                res=max(res,profit)
            
        if res<0:
            return 0
        return res
            