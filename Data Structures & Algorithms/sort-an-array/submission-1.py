class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=0
        while(n<len(nums)):          
            for i in range(0,len(nums)-1):
                    if(nums[i]>nums[i+1]):
                        temp=nums[i]
                        nums[i]=nums[i+1]
                        nums[i+1]=temp
            n+=1
        return nums
        