class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        size=1
        nums.sort()
        res=0
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]-nums[i-1]==1:
                size+=1
            else:
                res=max(res,size)
                size=1
        return max(res,size)

