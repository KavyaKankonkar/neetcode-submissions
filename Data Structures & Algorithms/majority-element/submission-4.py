class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm=defaultdict(int)
        l=len(nums)
        for n in nums:
            hm[n]+=1

        for n in nums:
            if (hm[n])>(l//2) :
                return n
                  