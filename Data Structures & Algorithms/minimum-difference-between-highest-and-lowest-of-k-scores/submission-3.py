class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res=float("inf")
        nums.sort()
        subset=[]
        l=0
        r=k-1
        while r<len(nums):
            subset=nums[l:r+1]
            d=max(subset)-min(subset)
            res=min(res,d)
            l+=1
            r+=1
            
        return int(res)




