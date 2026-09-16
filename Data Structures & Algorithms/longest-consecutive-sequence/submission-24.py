class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        numset=set(nums)
        longest=0

        for num in numset:
            if num-1 not in numset:
                l=1
                while num+l in numset:
                    l+=1
                longest=max(longest,l)

        return longest

