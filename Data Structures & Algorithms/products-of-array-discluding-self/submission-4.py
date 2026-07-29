class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preP=[1]*len(nums)
        suffP=[1]*len(nums)
        prod=1
        for i in range(len(nums)):
            for j in range(0,i):
                prod*=nums[j]
            preP[i]=prod
            prod=1

        prod=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod*=nums[j]
            suffP[i]=prod
            prod=1
        
        res=[]
        for i in range(len(nums)):
            res.append(preP[i]*suffP[i])
        
        return res
        
