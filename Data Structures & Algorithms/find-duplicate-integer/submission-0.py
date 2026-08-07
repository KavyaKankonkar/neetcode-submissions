class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs=set()

        for s in nums:
            if (s in hs):
                return s
            hs.add(s)

         