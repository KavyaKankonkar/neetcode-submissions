class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=[]
        sum=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
               res.append(prices[i+1]-prices[i])
        
        for i in res:
            sum+=i
        return sum
            