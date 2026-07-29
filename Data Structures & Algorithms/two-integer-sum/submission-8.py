class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        
        for i,n in enumerate(nums):
            v=target-n

            if v in hm:
                return [hm[v],i]
            hm[n]=i
        return []

