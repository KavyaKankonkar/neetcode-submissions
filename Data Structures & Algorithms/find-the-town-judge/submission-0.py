class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        ind=[0]*(n+1)
        oud=[0]*(n+1)

        for i in range(len(trust)):
            n1=trust[i][0]
            oud[n1]+=1
            
            n2=trust[i][1]
            ind[n2]+=1

        for i in range(1,len(oud)):
            if oud[i]==0 and ind[i]==n-1:
                return i
            
        
        return -1
                


            


                
