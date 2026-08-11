class Solution:
    def arrangeCoins(self, n: int) -> int:
        li=[]
        i=0
        res=0
        while n!=0:
            k=i+1
            
            if k<=n :
                li.append(k)
            else:
                break
            n-=(i+1)
            i+=1

        for i in li:
            res+=1
            
        return res
                

