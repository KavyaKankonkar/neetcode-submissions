class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[0]*len(nums)
        suf=[0]*len(nums)
        res=[0]*len(nums)
        n=len(nums)

        pre[0]=1

        suf[n-1]=1
        
        for i in range(1,n):
            pre[i]=nums[i-1]*pre[i-1]

        for j in range(n-2,-1,-1):
            suf[j]=nums[j+1]*suf[j+1]

        for k in range(n):
            res[k]=pre[k]*suf[k]

        return res


        
    
        
