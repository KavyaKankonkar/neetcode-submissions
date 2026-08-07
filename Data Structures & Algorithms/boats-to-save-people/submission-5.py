class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        max_w=max(people)
        count=[0]*(max_w+1)
        
        for val in people:
            count[val]+=1
        
        ind,i=0,1

        while (ind!=len(people)) :
            while count[i]==0:
                i+=1
            people[ind]=i
            count[i]-=1
            ind+=1

        l,r=0,len(people)-1
        res=0
        while l<=r:
            remain=limit-people[r]
            r-=1
            res+=1
            if l<=r and people[l]<=remain :
                l+=1
        
        return res