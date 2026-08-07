class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs={}
        li=[]
        for ind,val in enumerate(nums):
            n=target-val
            if n in hs:
                li= [hs[n],ind]
            hs[val]=ind
        
        return li