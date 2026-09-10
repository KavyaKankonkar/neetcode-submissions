class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l=len(nums)
        k=k%l

        def reverse(l:int, r:int)->None:
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1

        reverse(0,l-1)
        reverse(0,k-1)
        reverse(k,l-1)

    