class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=len(nums)-1

        hm={}

        for ind,val in enumerate(nums):
            if val not in hm:
                hm[val]=ind
            else:
                if abs(ind-hm[val])<=k :
                    return True
                hm[val]=ind
        return False
                    
