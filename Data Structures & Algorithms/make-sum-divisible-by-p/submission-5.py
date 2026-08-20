class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s=sum(nums)
        res=float("inf")
        siz=0
        su=0
        
        seen={0:-1}

        target=sum(nums)%p

        if target==0:
            return 0
        
        for i in range(len(nums)):
            su=su+nums[i]

            current_rem=su%p
            needed=(current_rem-target )%p

            if needed in seen:
                res=min(res,i-seen[needed])

            seen[current_rem]=i
            
        if res>=len(nums):
            return -1
        return int(res)
        
            