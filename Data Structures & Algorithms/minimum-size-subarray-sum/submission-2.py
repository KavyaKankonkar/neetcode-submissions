class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum=0
        l=0
        res=len(nums)+1

        for r in range(len(nums)):
            curSum+=nums[r] 
            while curSum>=target:
                res=min(res,r-l+1)
                curSum-=nums[l]
                l+=1

        if res!=len(nums)+1:
            return res
        else:
            return 0
        

        