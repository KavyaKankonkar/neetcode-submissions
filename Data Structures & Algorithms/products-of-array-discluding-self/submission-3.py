class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1,nums[0]]
        suffix=[]
        prod=1
        res=[]
        for i in range(2,len(nums)):            
            j=0
            while(j<i):
                prod=prod*nums[j]
                j+=1
            prefix.append(prod)
            prod=1

        for i in range(0,len(nums)):            
            j=len(nums)-1
            
            while(j>i):
                prod=prod*nums[j]
                j-=1
            if i==len(nums)-1:
                suffix.append(1)
            suffix.append(prod)
            prod=1
        
        for i in range(0,len(nums)):
            res.append(prefix[i]*suffix[i])   

        return res       

            

        