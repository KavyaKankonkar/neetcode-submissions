class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        hm={}
        res=[]
        for i in nums:
            hm[i]=hm.get(i,0)+1
        
        for ele,val in hm.items():
            if val>(n//3):
                res.append(ele)

        return res