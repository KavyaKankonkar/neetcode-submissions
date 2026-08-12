class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l=0
        r=len(prices)-1
        # prices.sort()
        cost=0
        p=0
        while l<r:
            c=prices[l]+prices[r]
            if c<=money and money-c>=0:
                p+=1
                cost=max(money-c,cost)
            if prices[l]<prices[r]:
                r-=1
            else:
                l+=1

        if p==0:
            return money
        return cost
            
        
        


