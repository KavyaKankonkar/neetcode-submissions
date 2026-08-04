class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l=0
        # r=len(nums)-1

        # while l<=r:
        #     mid=l+(l-r)//2
        res=1000
        for i in range(len(nums)):
            res=min(res,nums[i])

        return res

            