class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=0
        while(n<len(nums)):
            for i in range(0,len(nums)-1):
                if nums[i]>nums[i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp
            n=n+1
        
                
        