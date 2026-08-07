class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        long=0
        for i in nums:
            if i-1 not in hs:
                count=0
                while (i+count) in hs:
                    count+=1
                long=max(count,long)   

        return long         