class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        i=0
        while i<l:
            if i<len(nums):
                if nums[i]==val:
                    nums.remove(nums[i])
                    i-=1
                i+=1
            else:
                break

        # if nums[-1]==val:
        #     nums.remove(nums[-1])

        return len(nums)