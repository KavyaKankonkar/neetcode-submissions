class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float("inf")
        l=0
        r=k-1
        
        while r!=len(nums):
            ans=min(ans,nums[r]-nums[l])
            l+=1
            r+=1
            
        return ans

        
