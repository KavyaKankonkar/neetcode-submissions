class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        hs=[]
        for i in range(0,m):
            hs.append(nums1[i])

        for i in nums2:
            hs.append(i) 
        
        hs.sort()

        for i in range(0,m+n):
            nums1[i]=hs[i]

            