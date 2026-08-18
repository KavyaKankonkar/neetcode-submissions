class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l=0
        m=0
        r=1
        res=1
        ins,des=0,0

        while r<len(nums):
            if nums[m]<nums[r]:
                ins+=1
            else:
                ins=0
                l=m
            
            res=max(res,ins+1)
            m+=1
            r+=1
        k=1
        s=0
        mi=0
        while k<len(nums):
            if nums[mi]>nums[k]:
                des+=1
            else:
                des=0
                s=mi
                # continue
            res=max(res,des+1)
            mi+=1
            k+=1
        return res