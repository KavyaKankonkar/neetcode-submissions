class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind=0
        for i in range(len(nums)):
           if nums[i] !=val:
              nums[ind]=nums[i]
              ind=ind+1
        
        return ind 
