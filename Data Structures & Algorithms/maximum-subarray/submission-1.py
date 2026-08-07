class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        sub=nums[0]

        for i in range(1,len(nums)):
            n=i-1
            if sub<0:
                sub=nums[i]
            else:
                sub=sub+nums[i]
            res=max(res,sub)
        
        return res