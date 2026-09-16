class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stk=[]

        arr=[0]*len(prices)
        profit=[0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            if stk==[]:
                stk.append(prices[i])

            if stk[-1]>=prices[i]:
                arr[i]=stk[-1]
           
            else:
                while stk!=[] and prices[i]>stk[-1]:
                    stk.pop()
                
                if stk==[]:
                    arr[i]=0
                    stk.append(prices[i])
                else:
                    arr[i]=stk[-1]
                

        for i in range(len(prices)):
            profit[i]=arr[i]-prices[i]

        return max(profit)

            
                    
