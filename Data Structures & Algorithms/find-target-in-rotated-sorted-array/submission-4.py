class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            mid=l+(r-l)//2

            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        if target==nums[l]:
            return l
        k=l
        r=len(nums)-1
        ans=-1
        while l<=r:
            mid=l+(r-l)//2
            
            if nums[mid]==target:
                ans=mid
                return ans
            
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        if ans==-1:
            r=k-1
            k=0
            if nums[k]==target:
                ans=k
                return ans
            while k<=r:
                mid=k+(r-k)//2
                
                if nums[mid]==target:
                    ans=mid
                    return ans
                
                if nums[mid]>target:
                    r=mid-1
                else:
                    k=mid+1
            
        return -1
            

